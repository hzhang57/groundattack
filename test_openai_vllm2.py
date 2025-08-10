from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.distributed import DistributedConfig
import torch
 
model_path = "openai/gpt-oss-120b"
tokenizer = AutoTokenizer.from_pretrained(model_path, padding_side="left")
 
device_map = {
    # Enable Expert Parallelism
    "distributed_config": DistributedConfig(enable_expert_parallel=1),
    # Enable Tensor Parallelism
    "tp_plan": "auto",
}
 
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    attn_implementation="kernels-community/vllm-flash-attn3",
    **device_map,
)
 
messages = [
     {"role": "user", "content": "Explain how expert parallelism works in large language models."}
]
 
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
).to(model.device)
 
outputs = model.generate(**inputs, max_new_tokens=1000)
 
# Decode and print
response = tokenizer.decode(outputs[0])
print("Model response:", response.split("<|channel|>final<|message|>")[-1].strip())
