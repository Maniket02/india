import streamlit as st
import openai
import os

# ---------- CONFIG ----------
openai.api_key = "YOUR_OPENAI_API_KEY"

HISTORY_PATH = "history"

# ---------- READ HISTORY ----------
def load_history(era):
    file_path = os.path.join(HISTORY_PATH, f"{era}.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# ---------- CHATGPT QUERY ----------
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in Indian history."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"]

# ---------- STREAMLIT UI ----------
st.title("📚 Indian History Timeline Reader")

era_choice = st.selectbox(
    "Select an Era",
    ("ancient", "medieval", "modern")
)

# Show history timeline
history_text = load_history(era_choice)
st.subheader(f"{era_choice.capitalize()} Era Timeline")
st.text(history_text)

st.markdown("---")

# ---------- GPT Query ----------
st.subheader("Ask ChatGPT About Indian History")
user_question = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_question.strip():
        with st.spinner("Thinking..."):
            answer = ask_gpt(user_question)
        st.success(answer)
    else:
        st.error("Please enter a question.")
