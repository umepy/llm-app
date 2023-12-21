from openai import OpenAI

client = OpenAI(api_key="ここにAPIキーを入力")
model = "gpt-3.5-turbo"

def llm_response(chat_history):
    response = client.chat.completions.create(model=model, messages=chat_history)
    result = response.choices[0].message.content
    return result

