from google.cloud import aiplatform
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession
import streamlit as st

st.title("☃️ Maddie's Amazing Chatbot")

project_id = "quantum-backup-415716"
location = "us-central1"
vertexai.init(project=project_id, location=location)
model = GenerativeModel("gemini-1.0-pro")
chat = model.start_chat()

# Initialize the chat messages history
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How can I help?"}]

# Prompt for user input and save
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

# display the existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, we need to generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    # Call LLM
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            text_response = []
            r = chat.send_message(
                [m["content"] for m in st.session_state.messages],
                stream=True,
            )
            for chunk in r:
                text_response.append(chunk.text)
            st.write("".join(text_response))

    message = {"role": "assistant", "content": ("".join(text_response))}
    st.session_state.messages.append(message)
