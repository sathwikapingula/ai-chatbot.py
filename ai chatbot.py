import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"

)
#Title
st.title(" 🤖My AI Chatbot")
st.caption("powered by ollama + streamlit")

#Initlize conversation history
if "messages" not in st.session_state:
    st.session_state.messages=[]

#display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

#chat input
prompt=st.chat_input("type your message...")

if prompt:
    #store user message
    st.session_state.message.append({
        "role":"user",
        "content":prompt
    })
    #Display user message
    with st.chat_message("user"):
        st.write(prompt)

    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    #store AI response
    st.session_state.messages.append({
        "role":"assistant",
        "content":answer
    })

    #Display AI response
    with st.chat_message("assistant"):
        st.write(answer)
    