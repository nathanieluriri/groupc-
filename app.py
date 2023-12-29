import streamlit as st
from chating import display_previous_chats, user, bot_response
from auth0_component import login_button
from variables import text_for_tab_2, text_for_tab_1, text_for_tab_3, run_once, clientId,domainName, thinnk
from database import check_if_pk_exists, insert_into_user_reg, fk_status_profile_completeness, insert_into_ai_personalized_guide_for_users





    
st.set_page_config("Project",page_icon=":books:",layout="wide")



with st.sidebar:
    run_once()
    if st.session_state.signed_in == False:
        user_info = login_button(clientId = clientId, domain = domainName, key="login")
        st.session_state.user_info = user_info
        if user_info != False:
            st.session_state.signed_in = True
        elif user_info == False:
            st.session_state.signed_in = False


    


auth_state = None

# write logic for a logout 


if not st.session_state.user_info == False:
    auth_state = True
    pk_status = check_if_pk_exists(PK=st.session_state.user_info["sub"],YourTableName="Users",yourPrimaryKeyColumn="UserID")

    if pk_status == True: # after first time logging in
        
        profile_completeness= fk_status_profile_completeness(st.session_state.user_info['sub'])
        if profile_completeness ==True: # render ui for user with completed profile
            st.write(f"# Welcome Back {st.session_state.user_info['given_name']}")
            st.session_state.Prompt = st.chat_input("Detect Cyber Bullying In conversations")


            if st.session_state.Prompt:
                display_previous_chats()
                user(st.session_state.Prompt)
                Respond, Response = thinnk(st.session_state.Prompt)
                if Respond: # bot response consider adding logic to transform the response gotten from the ai to something more readeable and easier to visualize
                    bot_response(Response)
           




















        else: # Complete profile 
            st.info("After you click on submit you can only adjust the value once.")
            with st.container(border=True):
                
                st.subheader("Please complete your profile")
                tab1, tab2, tab3 = st.tabs(["Step 1", "Step 2", "Step 3"])
                with tab1:
                    st.code(text_for_tab_1)
                    st.slider(" ",1,5,key="reading_speed_slider",disabled=st.session_state.t1)
                    if st.button("Submit Reading Speed"):
                        st.session_state.t1 = True
                        st.write(st.session_state.reading_speed_slider)
                        
                    
                

                with tab2:
                    st.code(text_for_tab_2)
                    st.slider(" ",1,5,key="level_of_understanding_slider",disabled=st.session_state.t2)
                    if st.button("Submit Level Of Understanding"):
                        st.session_state.t2 = True
                        st.write(st.session_state.level_of_understanding_slider)

                with tab3:
                    st.code(text_for_tab_3 )
                    st.slider(" ",1,5,key="diction_slider",disabled=st.session_state.t3)
                    if st.button("Finish Profile"):
                        st.session_state.t3 = True
                        with st.spinner("Inserting Data into database..."):
                            insert_into_ai_personalized_guide_for_users(st.session_state.user_info["sub"],st.session_state.reading_speed_slider,st.session_state.level_of_understanding_slider,st.session_state.diction_slider)
                            st.success("Succesfully Completed Profile weldone")

                        

                

    else: # First time logining in
        st.write(f"# Nice to meet you {st.session_state.user_info['name']}")
        insert_into_user_reg(UserID=st.session_state.user_info["sub"],name=st.session_state.user_info["given_name"],email=st.session_state.user_info["email"] )
        st.success("You have Successfully logged in Please refresh and log in again")



if st.session_state.user_info == False:
    auth_state = False


        
if not st.session_state.user_info:
    st.write("# Please login to continue")



if auth_state == True:
    pass


