from openai import OpenAI

#from local_llm import get_local_llm_response
#from prompt import get_local_llm_prompt

client = OpenAI(api_key="ここにAPIキーを入力")

def llm_response(model_name, chat_history):
    model_name = model_name_convert(model_name)
    if model_name == "gpt-3.5-turbo" or model_name == "gpt-4-1106-preview":
        response = client.chat.completions.create(model=model_name, messages=chat_history)
        result = response.choices[0].message.content
    # elif model_name == "gpt-4-1106-preview":
    #     chat_history = get_local_llm_prompt(chat_history)
    #     result = get_local_llm_response(chat_history, model_name)
    else:
        raise

    return result

def model_name_convert(model_name):
    if model_name == "gpt-3.5":
        return "gpt-3.5-turbo"
    elif model_name == "gpt-4":
        return "gpt-4-1106-preview"
    else:
        raise ValueError("Unknown model name")
