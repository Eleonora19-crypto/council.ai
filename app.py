import streamlit as st
import openai
import os

# Setup
st.set_page_config(page_title="Council.ai", page_icon="🧠")
st.title("🎓 Council.ai")
st.subheader("Your AI-powered study assistant for SAT, TOEFL & more")

# API Key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Tabs
tab1, tab2, tab3 = st.tabs(["📘 SAT Quiz", "✍️ Essay Feedback", "🎯 College Matcher"])

with tab1:
    st.header("SAT-style Quiz")
    question = st.text_input("Type a topic or ask for a SAT practice question:")
    if st.button("Generate SAT Question"):
        with st.spinner("Generating..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a test-prep tutor. Give 1 SAT-style multiple choice question."},
                    {"role": "user", "content": question}
                ]
            )
            st.write(response["choices"][0]["message"]["content"])

with tab2:
    st.header("Essay Feedback")
    essay = st.text_area("Paste your essay here:")
    if st.button("Get Feedback"):
        with st.spinner("Analyzing..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're an English teacher. Give feedback on grammar, clarity, and structure."},
                    {"role": "user", "content": essay}
                ]
            )
            st.write(response["choices"][0]["message"]["content"])

with tab3:
    st.header("College Matcher")
    major = st.text_input("What do you want to study?")
    location = st.text_input("Preferred country or region?")
    if st.button("Find Colleges"):
        with st.spinner("Matching..."):
            prompt = f"I'm a student looking to study {major} in {location}. Suggest 3 good universities and explain why."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.write(response["choices"][0]["message"]["content"])
