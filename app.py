import streamlit as st

import prompt
from llm import llm_response

st.set_page_config(page_title="AIチャットアプリ")

if st.session_state.get("chat_messages") is None:
    st.session_state["chat_messages"] = [prompt.SYSTEM_PROMPT]

# sidebar
st.sidebar.title("設定")
st.session_state["model_name"] = st.sidebar.selectbox("AIモデル", ["gpt-3.5", "Swallow"])


st.subheader("AIとチャットする")

for message in st.session_state["chat_messages"]:
    if message["role"] == "system":
        continue
    st.chat_message(message["role"]).write(message["content"])

if message := st.chat_input():
    st.chat_message("user").write(message)
    st.session_state["chat_messages"].append({"role": "user", "content": message})

    ai_response = llm_response(st.session_state["model_name"],st.session_state["chat_messages"])
    st.chat_message("assistant").write(ai_response)
    st.session_state["chat_messages"].append({"role": "assistant", "content": ai_response})
