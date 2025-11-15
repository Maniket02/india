from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in Indian history."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

HISTORY_PATH = "history"

def load_history(era):
    file_path = os.path.join(HISTORY_PATH, f"{era}.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in Indian history."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

st.title("📚 Indian History Timeline Reader")

era_choice = st.selectbox("Select an Era", ("ancient", "medieval", "modern"))

history_text = load_history(era_choice)
st.subheader(f"{era_choice.capitalize()} Era Timeline")
st.text(history_text)

st.markdown("---")

st.subheader("Ask ChatGPT About Indian History")
question = st.text_input("Your question:")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = ask_gpt(question)
        st.success(answer)
    else:
        st.error("Please enter a question.")
