import os
from swift.llm import PtEngine, RequestConfig, InferRequest

#os.environ['CUDA_VISIBLE_DEVICES'] = '1'
os.environ['MAX_PIXELS'] = '409600' #'1003520'
os.environ['VIDEO_MAX_PIXELS'] = '50176'
os.environ['FPS_MAX_FRAMES'] = '10'

class vlm_qwen:
    ## Qwen2.5-VL系列模型的输入格式是<image>+question, 需要<image>的placeholder，数量与len(images)一致
    def __init__(self, model_path="Qwen/Qwen2.5-VL-7B-Instruct", print_process=False):
        self.engine = PtEngine(model_path, max_batch_size=1)
        self.request_config = RequestConfig(max_tokens=512, temperature=0)
        self.print_process = print_process

    def predict(self, images, question):
        ## question 的格式是<image>+question, 需要<image>的placeholder，数量与len(images)一致
        infer_requests = [
            InferRequest(messages=[{'role': 'user', 'content': question}],
                 images=images),
    ]

        answer = self.engine.infer(infer_requests, self.request_config)
        answer = answer[0].choices[0].message.content

        if self.print_process:
            print("*"*10)
            print("Question: {}\n".format(question))
            print("Inference: {}\n".format(infer_requests))
            print("Answer:{}\n".format(answer))

        return answer
    def text_predict(self, question):
        infer_requests = [
            InferRequest(messages=[{'role': 'user', 'content': question}])]

        answer = self.engine.infer(infer_requests, self.request_config)
        answer = answer[0].choices[0].message.content

        if self.print_process:
            print("*"*10)
            print("Question: {}\n".format(question))
            print("Inference: {}\n".format(infer_requests))
            print("Answer:{}\n".format(answer))

        return answer


if __name__ == "__main__":
    vlm_qwen = vlm_qwen(print_process=True)
    ##测试文本
    vlm_qwen.predict([], "What is the capital of France?")
    vlm_qwen.text_predict("What is the capital of France?")

    ##测试图片
    from vlm_utils import load_image
    image = load_image("cat.jpg")
    vlm_qwen.predict([image, image], "What is in the image<image><image>\n?")
    #vlm_qwen.predict([image], "What is in <image>\nthe image?")
    #vlm_qwen.predict([image], "What is in the image<image>\n?")
    #vlm_qwen.predict([image], "What is in the image<image>?")
    #vlm_qwen.predict([image], "")
    #vlm_qwen.predict([image], "<image>\n")
    #vlm_qwen.predict([image], "<image><image>\n")
    #vlm_qwen.predict([], "What is in the image<image>?")
    #vlm_qwen.predict([], "What is in the <image>?")
    #vlm_qwen.predict([], "What is in the image?")
    #vlm_qwen.predict([], "What is in the ?")
    #vlm_qwen.predict([], "What is <image>?")
