import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

local_llm = None
local_tokenizer = None

def get_local_llm(model_name:str):
    global local_llm
    global local_tokenizer
    if local_llm is None:
        local_tokenizer = AutoTokenizer.from_pretrained(model_name)
        local_llm = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, device_map="auto")


def get_local_llm_response(chat_history, model_name:str):
    global local_llm
    global local_tokenizer
    if local_llm is None or local_tokenizer is None:
        get_local_llm(model_name)
    assert local_llm is not None and local_tokenizer is not None
    input_ids = local_tokenizer.encode(chat_history, add_special_tokens=False, return_tensors="pt")
    output_ids = local_llm.generate(input_ids.to(device=local_llm.device), do_sample=True, max_length=512,temperature=0.99,top_p=0.95)
    result = local_tokenizer.decode(output_ids[0], skip_special_tokens=True)
    result = result[len(chat_history):]
    return result


if __name__=="__main__":
    model_name = "tokyotech-llm/Swallow-7b-instruct-hf"
    result = get_local_llm_response("こんにちは", model_name)
    print(result)
