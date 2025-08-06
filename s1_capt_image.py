import os
from vlm import vlm_qwen, load_image
from captioner import caption_wrapper
from captioner import image_caption_prompt

os.environ['CUDA_VISIBLE_DEVICES'] = '1'
os.environ['MAX_PIXELS'] = '409600' #'1003520'
os.environ['VIDEO_MAX_PIXELS'] = '50176'
os.environ['FPS_MAX_FRAMES'] = '10'
def main():
    # 初始化VLM模型
    vlm = vlm_qwen()
    # 将vlm装入captioner里作为引擎
    captioner = caption_wrapper(vlm_model=vlm, caption_prompt=image_caption_prompt, print_process=True)
    ## 测试功能 to delete
    image = load_image("./vlm/cat.jpg")
    images = [image]
    text = captioner.generate_caption(images)
    ## 加载数据

    ## 数据清洗


    print("Process finished, bravo!")

if __name__ == "__main__":
    main()