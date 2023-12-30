import pandas as pd
import streamlit as st
import random as rd

def generate_bar_chart(testing):
    try:
        if "1" in testing and "^" in testing and "*" in testing and "@" in testing and "&" in testing:  # No chance of not bullying context
            d = {"Cyberbullying": [rd.randint(75, 100)], "Not cyberbullying": [rd.randint(0, 15)]}
            data = pd.DataFrame(data=d)
            return data

        elif "0" in testing and "^" in testing and "*" in testing and "@" in testing and "&" in testing:  # No chance of bullying context
            
            d = {"Cyberbullying": [rd.randint(0, 15)], "Not cyberbullying": [rd.randint(70, 95)]}
            data = pd.DataFrame(data=d)
            return data

        elif "0" in testing and "^" in testing and "@" in testing and "&" in testing:  # higher no bullying chance than bullying chance but keep it in a 68,32 range
            
            d = {"Cyberbullying": [rd.randint(12, 28)], "Not cyberbullying": [rd.randint(32, 68)]}
            data = pd.DataFrame(data=d)
            return data

        elif "1" in testing and "^" in testing and "@" in testing and "&" in testing:  # higher bullying chance than bullying chance but keep it in a 68,32 range
            d = {"Cyberbullying": [rd.randint(32, 68)], "Not cyberbullying": [rd.randint(10, 28)]}
            data = pd.DataFrame(data=d)
            return data

    except TypeError:
        return None

# Example usage:
# testing_value = st.chat_input("enter a number between 1 and 0")
# chart_data = generate_bar_chart(testing_value)

# if chart_data is not None:
#     st.bar_chart(chart_data)

def response_calculator(res):
        if "1" in res and "^" in res and "*" in res and "@" in res and "&" in res:  # No chance of not bullying context
            response = ["There is almost no way the text here was meant to bully someone","The text wey dey here no too get wahala, e no look like say dem get intention to bully anybody.","E go hard make person see this text as bully, e dey show say dem just dey normal.","E dey very unlikely say the person get mind to bully with this text; e just dey simple and jejely.","There's a very low probability that the text was meant to bully someone; it appears quite benign.","It's unlikely that the author's intention in this text was to engage in bullying behavior.","The probability of the text being intended as a form of bullying is extremely low.","It's hard to interpret the text as a means of bullying; the likelihood of that intention is minimal.","This text no too carry signs wey fit mean say dem wan use am bully person.","The person wey write this text no too carry bad mind, e no resemble person wey wan bully","The text doesn't convey any significant signs of being intended as a form of bullying.","It's highly improbable that the text is meant to bully; the intent behind it seems incongruent with such behavior.","hmmm you sef look at the stat's","Oga no dey ask some kind questions"]
            return response[rd.randint(0,13)]

        elif "0" in res and "^" in res and "*" in res and "@" in res and "&" in res:  # No chance of bullying context
            
            response = ["There's an extremely low likelihood that the text here was intended to bully someone.","The text wey dey here no get wahala, e no show like say dem get intention to bully person.","It's quite easy for someone to see this text as anything but a form of bullying; e dey like say dem just dey use style for normal discussion.","The person no fit get mind to bully with this text; e dey simple and jejely.","The probability of the text being intended as a form of bullying is very low; e dey benign.","It's unlikely that the author's intention in this text was to engage in bullying behavior.","The probability of the text being intended as a form of bullying is extremely low; e no fit get any bad intention.","It no fit hard to interpret the text as anything other than a normal conversation; e no get serious likelihood of being bullying.","This text no dey carry signs wey fit mean say dem wan use am bully person; e just dey normal.","The person wey write this text no fit carry bad mind; e no resemble person wey wan bully.","The text no dey carry any serious signs of being intended as a form of bullying.","It no fit be say the text na intentional bully; the intent behind am no dey congruent with such behavior.","Hmmm, if you check the stats well, e be like say person no get mind to throw any kind cyber punch.","Oga, you no dey ask some kind questions wey fit show say you wan provoke person."]
            return response[rd.randint(0,13)]


        elif "0" in res and "^" in res and "@" in res and "&" in res:  # higher no bullying chance than bullying chance but keep it in a 68,32 range
            
            response = ["There's a possibility that the text here was intended to spark interest.","The text wey dey here get some depth; e fit be say dem get intention to engage someone's thoughts.","It might be challenging for someone to interpret this text as anything other than potentially thought-provoking; e dey like say dem just dey use style.","The person fit get mind to generate discussion with this text; e no too dey simple and jejely.","The probability of the text being intended as thought-provoking is quite notable; e no too dey benign at all.","It's possible that the author's intention in this text was to evoke a reaction.","The probability of the text being intended as thought-provoking is not extremely low; e fit carry some tension.","It might be challenging to interpret the text as anything other than a means of sparking interest; e get a serious likelihood.","This text dey carry signs wey fit mean say dem wan add some flavor to am; e no just dey normal.","The person wey write this text fit carry some strong vibes; e resemble person wey wan stimulate some thoughts.","The text dey carry some serious signs of being intended as thought-provoking.","It might be the case that the text is intentionally engaging; the intent behind am dey congruent with such expression.","Hmmm, if you check the stats well, e be like say person get mind to make some bold but insightful statements.","Oga, no dey ask some kind questions wey fit show say you wan start some thoughtful discussion."]
            return response[rd.randint(0,13)]


        elif "1" in res and "^" in res and "@" in res and "&" in res:  # higher bullying chance than bullying chance but keep it in a 68,32 range
            response = ["There's a significant likelihood that the text here was intended to bully someone.","The text wey dey here get serious wahala, e show like say dem get strong intention to bully person.","It fit hard person to see this text as anything but a form of intense bullying; e dey like say dem just dey use style.","The person fit get strong mind to bully with this text; e no too dey simple and jejely.","The probability of the text being intended as a form of bullying is notably high; e no dey benign at all.","It's quite likely that the author's intention in this text was to engage in aggressive behavior and bullying.","The probability of the text being intended as a form of bullying is not extremely low; e fit get some bad and intense intention.","It fit hard to interpret the text as anything other than a means of serious bullying; e get a serious likelihood.","This text dey carry signs wey fit mean say dem wan use am bully person; e no just dey normal.","The person wey write this text fit carry strong bad mind; e resemble person wey wan bully intensely.","The text dey carry some serious signs of being intended as a form of intense bullying.","It fit be say the text na intentional bully; the intent behind am dey congruent with such intense behavior.","Hmmm, if you check the stats well, e be like say person get strong mind to throw some kind cyber punches.","Oga, no dey ask some kind questions wey fit show say you wan provoke person with serious vibes."]
            return response[rd.randint(0,13)]


if "messages" not in st.session_state:
    st.session_state.messages = []

if "message_charts" not in st.session_state:
    st.session_state.message_charts = []

def display_previous_chats ():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant":
                st.bar_chart(message["Chart"])


def user(Prompt):
    if "messages" not in st.session_state:
        st.session_state.messages = []
    user_prompt = st.chat_message("user")
    user_prompt.write(Prompt)
    st.session_state.messages.append({"role":"user","content":Prompt,"Chart":None})



def bot_response(Prompt,data):
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "message_charts" not in st.session_state:
        st.session_state.message_charts = []

    bot_res = st.chat_message("assistant")
    The_gist = response_calculator(Prompt)
    
    bot_res.write(The_gist)
    bot_res.bar_chart(data,use_container_width=True)
    st.session_state.messages.append({ "role":"assistant", "content":The_gist, "Chart":data })
