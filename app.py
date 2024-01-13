import streamlit as st
from chating import display_previous_chats, user, bot_response, generate_bar_chart
from variables import thinnk


st.set_page_config("Project", page_icon=":books:", layout="wide")

# Simulated authentication state
auth_state = True  # Simulating authentication by default
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .viewerBadge_link__qRIco{display:None;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
if "messages" not in st.session_state:
    st.session_state.messages = []
# Simulated user_info
st.session_state.user_info = {"sub": "123", "given_name": "User", "email": "john@example.com"}

if auth_state:
    profile_completeness = True  # Simulating profile completeness
    
    if profile_completeness:
        
        st.success("Enter a chat to the chat input bar and press enter or tap the arrow")
        st.write(f"# Welcome Back {st.session_state.user_info['given_name']}")
        st.session_state.Prompt = st.chat_input("Detect Cyber Bullying In conversations")
        display_previous_chats()

        if st.session_state.Prompt:
            st.info("TAP ON THE BAR CHART IT'S INTERACTIVE",icon="ℹ️")
            
            user(st.session_state.Prompt)
            Respond, Response = thinnk(st.session_state.Prompt)
            if Respond:
                data_ = generate_bar_chart(Response)
                bot_response(Response,data_)
    else:
        st.info("Please complete your profile")
        # Simulated profile completion steps
        # ...

# Simulated logout button
if not st.session_state.user_info:
    st.write("# Please login to continue")
