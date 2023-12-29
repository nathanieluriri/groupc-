import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

def display_previous_chats ():
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])



def user(Prompt):
    user_prompt = st.chat_message("user")
    user_prompt.write(Prompt)
    st.session_state.messages.append({"role":"user","content":Prompt})
def bot_response(Prompt):
    user_prompt = st.chat_message("assistant")
    user_prompt.write(Prompt)
    st.session_state.messages.append({"role":"assistant","content":Prompt})