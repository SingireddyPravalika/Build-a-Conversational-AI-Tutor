import streamlit as st
import google.generativeai as genai

# Title styling
st.markdown(
    """
    <style>
        .title-text {
            color: darkpurple;
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            padding: 20px;
        }
        
    </style>
    """
    , unsafe_allow_html=True
)

#Title
st.markdown('<p class="title-text">🌟Conversational AI Data Science Tutor🌟</p>', unsafe_allow_html=True)

# Read the API key
f = open(r"C:\Users\lavak\OneDrive\Desktop\DataScience Course\internship\TASKS\Task 6 - Build a Conversational AI Tutor\gemini.txt")
key = f.read()

#Configure the API Key
genai.configure(api_key=key)

#Init a gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction= "I am here to help you. Feel free to ask me anything related to Data Science."
                              )

# Initialize chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
                           
# Init the chat object
chat = model.start_chat(history=st.session_state["chat_history"])
st.chat_message("AI-Data Science Tutor").write("Hi there! How can I help you today? ")

for message in chat.history:
    sender = "AI-Data Science Tutor" if message.role == "model" else message.role
    st.chat_message(sender).write(message.parts[0].text)

user_input = st.chat_input()

if user_input:
    st.chat_message("user").write(user_input)
    response = chat.send_message(user_input)
    AC=st.chat_message("AI-Data Science Tutor").write(bot.text for bot in response)
    st.session_state["chat_history"] = chat.history
