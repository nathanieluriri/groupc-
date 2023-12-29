import streamlit as st
from chating import display_previous_chats, user, bot_response
from variables import text_for_tab_2, text_for_tab_1, text_for_tab_3, thinnk
from database import insert_into_ai_personalized_guide_for_users

st.set_page_config("Project", page_icon=":books:", layout="wide")

# Simulated authentication state
auth_state = True  # Simulating authentication by default

# Simulated user_info
st.session_state.user_info = {"sub": "123", "given_name": "master", "email": "john@example.com"}

if auth_state:
    profile_completeness = True  # Simulating profile completeness

    if profile_completeness:
        st.write(f"# Welcome Back {st.session_state.user_info['given_name']}")
        st.session_state.Prompt = st.chat_input("Detect Cyber Bullying In conversations")

        if st.session_state.Prompt:
            display_previous_chats()
            user(st.session_state.Prompt)
            Respond, Response = thinnk(st.session_state.Prompt)
            if Respond:
                bot_response(Response)
    else:
        st.info("Please complete your profile")
        # Simulated profile completion steps
        # ...

# Simulated logout button
if not st.session_state.user_info:
    st.write("# Please login to continue")
