import os
from vlm import vlm_qwen, load_image

os.environ['CUDA_VISIBLE_DEVICES'] = '1'
os.environ['MAX_PIXELS'] = '409600' #'1003520'
os.environ['VIDEO_MAX_PIXELS'] = '50176'
os.environ['FPS_MAX_FRAMES'] = '10'
def main():
    # 初始化VLM模型
    vlm = vlm_qwen()
    # 测试
    vlm.predict([], "What is the capital of France?")


    print("Process finished, bravo!")

if __name__ == "__main__":
    main()