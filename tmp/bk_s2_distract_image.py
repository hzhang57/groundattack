import os
import argparse
#from vlm import vlm_qwen, load_image, gpt_oss_120b
from vlm.llm_gpt_oss import gpt_oss_120b
#from captioner import caption_wrapper
#from captioner import image_caption_prompt
#from datasets import load_dataset
#from data_utils import format_mmstar_dataset
from distractor.distractor_wrapper import distractor_wrapper
from distractor.distractor_prompts import negative_prompt_128

import json
#from PIL import Image
from tqdm import tqdm


#os.environ['CUDA_VISIBLE_DEVICES'] = '1'
os.environ['MAX_PIXELS'] = '409600' #'1003520'
os.environ['VIDEO_MAX_PIXELS'] = '50176'
os.environ['FPS_MAX_FRAMES'] = '10'
def main():
    #参数
    parser = argparse.ArgumentParser()
    parser.add_argument("--caption-model-path", type=str, default="Qwen/Qwen2.5-VL-7B-Instruct")
    parser.add_argument("--distractor-model-path", type=str, default="openai/gpt-oss-120b")
    #parser.add_argument("--distractor-model-path", type=str, default="openai/gpt-oss-20b")
    parser.add_argument("--hf-dataset", type=str, default="Lin-Chen/MMStar")
    args = parser.parse_args()
    # 初始化VLM模型
    ##if "Qwen" in args.caption_model_path:
    ##    vlm = vlm_qwen(model_path=args.caption_model_path)
    ### 将vlm装入captioner里作为引擎
    ##captioner = caption_wrapper(vlm_model=vlm, caption_prompt=image_caption_prompt, print_process=False)
    ##print("[INFO: Captioner] Loaded VLM {}".format(args.caption_model_path))


    # 加载数据, 会自动下载数据集, loaddataset 
    #dataset = load_dataset(args.hf_dataset)['val']
    #n_vals  = len(dataset)
    #print("[INFO: Dataset] Loaded {}, with {} samples".format(args.hf_dataset, n_vals))

    ###################
    ## 数据清洗
    ##################
    data_repo = "./data_repo/"
    data_file = data_repo + "F0_mmstar.json"
    image_folder = data_repo + "F0_mmstar_images"
    if "MMStar" in args.hf_dataset:
        if os.path.exists(data_file):
            print("[INFO: Dataset] Found data file, loading...")

    ## 1. Caption 生成描述
    caption_file = data_repo + "F1_mmstar_caption.json"
    if "MMStar" in args.hf_dataset:
        if os.path.exists(caption_file):
            print("[INFO: Dataset] Found caption file".format(caption_file))

    ## 2 Distractor, 生成难的负样本
    ## 使用OpenAI的ChatGPT生成Hard-Negatives
    if "gpt-oss" in args.distractor_model_path:
        llm = gpt_oss_120b(model_path=args.distractor_model_path)
    distractor = distractor_wrapper(llm_model=llm, distractor_prompt=negative_prompt_128, print_process=True)
    print("[INFO: Distractor] Loaded LLM {}".format(args.distractor_model_path))

    distract_file = data_repo + "F2_mmstar_distract.json"
    if "MMStar" in args.hf_dataset:
        if os.path.exists(distract_file):
            print("[INFO: Dataset] Found distract file".format(distract_file))
        else:
            ## Load F0_mmstar.json
            f2_json = []
            with open(caption_file, "r") as f:
                f1_json = json.load(f)

            for ii, a_sample in enumerate(tqdm(f1_json, desc="Distract...")):
                #if ii > 10:
                #    break

                new_negatives = distractor.generate_negatives(a_sample["caption"], a_sample['only_question'], a_sample['only_answer'])
                a_sample["new_negatives"] = new_negatives
                f2_json.append(a_sample) ## Add captions to the sample

            ## save f1_json into caption file in a beautiful json format
            with open(distract_file, "w") as f:
                json.dump(f2_json, f, indent=2)


    ## 存入字典

    ## 写入文件

    ## 测试功能 to delete
    #image = load_image("./vlm/cat.jpg")
    #images = [image]
    #text = captioner.generate_caption(images)


    print("Process finished, bravo!")

if __name__ == "__main__":
    main()
