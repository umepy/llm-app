from openai import OpenAI

from local_llm import get_local_llm_response
from prompt import get_local_llm_prompt

client = OpenAI(api_key="ここにAPIキーを入力")
model = "gpt-3.5-turbo"

def llm_response(model_name, chat_history):
    model_name = model_name_convert(model_name)
    if model_name == "gpt-3.5-turbo":
        response = client.chat.completions.create(model=model, messages=chat_history)
        result = response.choices[0].message.content
    elif model_name == "tokyotech-llm/Swallow-7b-instruct-hf":
        chat_history = get_local_llm_prompt(chat_history)
        result = get_local_llm_response(chat_history, model_name)
    else:
        raise

    return result

def model_name_convert(model_name):
    if model_name == "gpt-3.5":
        return "gpt-3.5-turbo"
    elif model_name == "Swallow":
        return "tokyotech-llm/Swallow-7b-instruct-hf"
    else:
        raise ValueError("Unknown model name")
