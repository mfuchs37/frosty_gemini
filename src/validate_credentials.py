import streamlit as st

from google.cloud import aiplatform
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession

conn = st.connection("snowflake")
df = conn.query("select current_warehouse()")
st.write(df)

# TODO(developer): Update and un-comment below lines
project_id = "quantum-backup-415716"
location = "us-central1"
vertexai.init(project=project_id, location=location)
model = GenerativeModel("gemini-1.0-pro")
chat = model.start_chat()


def get_chat_response(chat: ChatSession, prompt: str) -> str:
    text_response = []
    responses = chat.send_message(prompt, stream=True)
    for chunk in responses:
        text_response.append(chunk.text)
    return "".join(text_response)


prompt = "What is Streamlit?"
st.write(get_chat_response(chat, prompt))
