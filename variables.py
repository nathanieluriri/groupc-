import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()


def trial():
    user_input = input("enter Prompt")
    done_thinking,response =thinnk(user_input)
    if done_thinking:
        print(response)

    else: print("someothing went wrong")


def thinnk(user_):
    response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-1106:group-c::8YTKwLjB",
    messages=[
        {"role": "system", "content": "You are a school guidance counsellor on the lookout for chats that hint of cyberbullying in a WhatsApp group chat."},
        {"role": "user", "content": user_}
    ]
    )
    ai_response = response.choices[0].message.content
    return True , ai_response




















clientId = 'YexToZlUgbRsHRjbzy8yckhAoegwQEcX'
domainName = 'dev-r7cupi8h76qk3w31.us.auth0.com'

text_for_tab_1 ="""
Select a value to help your bot know 
how fast you read, speed increases from 1
for very slow readers up to 5 for very fast reader"""

text_for_tab_2 ="""Opt for 1 if you typically require additional time when learning 
new things, or select 5 if acquiring new knowledge comes effortlessly 
to you.
                            
                             """
text_for_tab_3 ="""
Please indicate a value that 
reflects your current proficiency in English 
for your bot's understanding. 
Choose 1 if your vocabulary is fundamental, 
or select 5 if you appreciate 
using extensive and sophisticated language."""



def run_once():
    if "user_info" not in st.session_state:
        st.session_state.user_info = False


    if "signed_in" not in st.session_state:
        st.session_state.signed_in = False

    if "t2" and "t1" and "t3" not in st.session_state:
        st.session_state.t1 = False
        st.session_state.t2 = False
        st.session_state.t3 = False

    if "Prompt" not in st.session_state:
        st.session_state.Prompt = False

    if "messages" not in st.session_state:
        st.session_state.messages = []

    