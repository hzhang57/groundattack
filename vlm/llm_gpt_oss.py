from transformers import pipeline
import torch
import os
import openai
from openai import OpenAI
#os.environ['CUDA_VISIBLE_DEVICES'] = '3,4,5,6,7'
class gpt_oss_120b:
    ## gpt_oss_120b的模型
    ## 输入是文本，输出是文本
    def __init__(self, model_path="openai/gpt-oss-120b", print_process=False):
        self.pipe = pipeline("text-generation", model=model_path, 
                torch_dtype='auto', device_map="auto")

        self.print_process = print_process

    def text_predict(self, question):
        ## question 的格式是文本
        messages = [
            {"role": "user", "content": question,
             "chat_template_kwargs": {"enable_thinking": False}
            },
        ]

        outputs = self.pipe(
            messages,
            max_new_tokens=10240,
        )
        #print("*****")
        answer = outputs[0]["generated_text"][-1]['content']
        return answer


class gpt_4o_mini:

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def text_predict(self, question):
        response = self.client.responses.create(
            model="gpt-4o-mini",
            input=question
        )
        return response.output_text


#if __name__ == "__main__":
    #model = gpt_oss_120b()
    #question ="What is the capital of France?"
    #print(model.text_predict(question))

    #model = gpt_4o_mini("")
    #question ="What is the capital of France?"
    #response = model.text_predict(question)
    #print(response)