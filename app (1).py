
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Study Assistant")
st.write("An AI-powered study assistant for students.")

st.divider()

# API Key
api_key = st.text_input(
    "🔑 Enter your Gemini API Key",
    type="password"
)

if api_key:

    client = genai.Client(api_key=api_key)

    st.success("API key entered successfully!")

    question = st.text_area(
        "📝 Enter your question:",
        placeholder="Example: Explain Ohm's Law in simple words.",
        height=150
    )

    difficulty = st.selectbox(
        "🎯 Select difficulty level:",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("✨ Generate Answer", use_container_width=True):

        if question.strip() == "":
            st.warning("⚠️ Please enter a question.")

        else:

            prompt = f"""
You are an AI Study Assistant helping a university student.

Student's Question:
{question}

Student's Difficulty Level:
{difficulty}

Provide the response in the following format:

## Simple Explanation
Explain the concept clearly and in easy language.

## Key Points
Give 4 to 5 important points.

## Example
Give one simple practical example.

## Quick Revision
Give a short revision summary.

## Practice Questions
Give 3 questions for the student to practice.

Make the answer educational, accurate,
well-structured and easy to understand.
"""

            with st.spinner("🤖 AI is generating your answer..."):

                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                )

            st.divider()

            st.subheader("🤖 AI Answer")

            st.markdown(response.text)

else:

    st.info("👆 Please enter your Gemini API key to start.")

st.divider()

st.caption(
    "AI Study Assistant | Python + Streamlit + Gemini"
)
