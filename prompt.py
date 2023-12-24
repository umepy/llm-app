SYSTEM_PROMPT = {"role":"system", "content":"あなたは厳しい軍隊の鬼教官です。鬼教官の話し方でユーザと会話してください。"}

def get_local_llm_prompt(chat_history):
    prompt_template = """以下に、あるタスクを説明する指示があり、それに付随する入力が更なる文脈を提供しています。
リクエストを適切に完了するための回答を記述してください。\n\n
### 指示:\n{instruction}\n\n### 入力:\n{input}\n\n### 応答:\n"""
    inputs = ""
    for message in chat_history[1:]:
        inputs += f"{message['role']}:{message['content']}\n"
    prompt = prompt_template.format(instruction=chat_history[0]["content"], input=inputs)
    return prompt
