from transformers import pipeline
import torch
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '3,4,5,6,7'
model_id = "openai/gpt-oss-120b"

pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "user", "content": "Explain quantum mechanics clearly and concisely.",
     "chat_template_kwargs": {"enable_thinking": False}
},
]

outputs = pipe(
    messages,
    max_new_tokens=256,
)
print("*****")
print(outputs[0]["generated_text"][-1])
print(pipe.model.config._attn_implementation)



