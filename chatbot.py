import google.generativeai as genai
import streamlit as st

# Google API Key and Model Configuration
Google_API_Key = "AIzaSyCqk0SYqj5g4wXdVsj5nD3JH1KqBBZ6NiQ"
genai.configure(api_key=Google_API_Key)

# Model initiate
model = genai.GenerativeModel('gemini-1.5-flash')

def GetResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit interface
st.set_page_config(page_title="Simple ChatBot", layout="centered")

st.title("🎉 Simple Chatbot 🎉")
st.write("Powered by Google Generative AI")

# Initialize history in session state if not already initialized
if "history" not in st.session_state:
    st.session_state["history"] = []

# Custom CSS for chat bubbles and layout
st.markdown("""
    <style>
    .user-bubble {
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 10px;
        max-width: 70%;
        margin: 10px 0;
        align-self: flex-end;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .bot-bubble {
        background-color: #F0F0F0;
        padding: 10px;
        border-radius: 10px;
        max-width: 70%;
        margin: 10px 0;
        align-self: flex-start;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    </style>
""", unsafe_allow_html=True)

# Display chat history with styled bubbles
for user_msg, bot_response in st.session_state["history"]:
    st.markdown(f"<div class='chat-container'><div class='user-bubble'>🙂 {user_msg}</div></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-container'><div class='bot-bubble'>🤖 {bot_response}</div></div>", unsafe_allow_html=True)

# Chat form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000, placeholder="Type your message here...")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = GetResponseFromModel(user_input)
            st.session_state["history"].append((user_input, response))

            # Display the latest response immediately
            st.markdown(f"<div class='chat-container'><div class='user-bubble'>🙂 {user_input}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='chat-container'><div class='bot-bubble'>🤖 {response}</div></div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a message.")
