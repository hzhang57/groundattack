import os
import argparse
from vlm import vlm_qwen, load_image
from captioner import caption_wrapper
from captioner import image_caption_prompt
from datasets import load_dataset
from data_utils import format_mmstar_dataset
import json
from PIL import Image
from tqdm import tqdm


os.environ['CUDA_VISIBLE_DEVICES'] = '1'
os.environ['MAX_PIXELS'] = '409600' #'1003520'
os.environ['VIDEO_MAX_PIXELS'] = '50176'
os.environ['FPS_MAX_FRAMES'] = '10'
def main():
    #参数
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, default="Qwen/Qwen2.5-VL-7B-Instruct")
    parser.add_argument("--hf-dataset", type=str, default="Lin-Chen/MMStar")
    args = parser.parse_args()
    # 初始化VLM模型
    if "Qwen" in args.model_path:
        vlm = vlm_qwen(model_path=args.model_path)
    # 将vlm装入captioner里作为引擎
    captioner = caption_wrapper(vlm_model=vlm, caption_prompt=image_caption_prompt, print_process=False)
    print("[INFO: Captioner] Loaded VLM {}".format(args.model_path))
    # 加载数据, 会自动下载数据集, loaddataset 
    dataset = load_dataset(args.hf_dataset)['val']
    n_vals  = len(dataset)
    print("[INFO: Dataset] Loaded {}, with {} samples".format(args.hf_dataset, n_vals))

    ###################
    ## 数据清洗
    ##################
    data_repo = "./data_repo/"
    data_file = data_repo + "F0_mmstar.json"
    image_folder = data_repo + "F0_mmstar_images"
    if "MMStar" in args.hf_dataset:
        if os.path.exists(data_file):
            print("[INFO: Dataset] Found data file, loading...")
        else:
            f0_json = format_mmstar_dataset(dataset, data_file, image_folder).format()
            ## save f0_json into data_file in a beautiful json format
            with open(data_file, "w") as f:
                json.dump(f0_json, f, indent=2)
                print("[INFO: Saved MMStar dataset to {}]".format(data_file))


    ## 生成描述
    caption_file = data_repo + "F1_mmstar_caption.json"
    if "MMStar" in args.hf_dataset:
        if os.path.exists(caption_file):
            print("[INFO: Dataset] Found caption file".format(cation_file))
        else:
            ## Load F0_mmstar.json
            f1_json = []
            with open(data_file, "r") as f:
                f0_json = json.load(f)
            
            for ii, a_sample in enumerate(tqdm(f0_json, desc="Captioning...")):
                #if ii > 10:
                #    break

                image_file = image_folder + "/" + a_sample["image"]
                image = Image.open(image_file)
                images = [image]
                caption_text = captioner.generate_caption(images)
                a_sample["caption"] = caption_text
                print("caption: {}".format(caption_text))
                f1_json.append(a_sample) ## Add captions to the sample

            ## save f1_json into caption file in a beautiful json format
            with open(caption_file, "w") as f:
                json.dump(f1_json, f, indent=2)


        
            


    ## 存入字典

    ## 写入文件

    ## 测试功能 to delete
    #image = load_image("./vlm/cat.jpg")
    #images = [image]
    #text = captioner.generate_caption(images)


    print("Process finished, bravo!")

if __name__ == "__main__":
    main()