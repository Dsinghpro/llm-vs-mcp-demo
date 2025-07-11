import streamlit as st
import asyncio
from openai_client import call_openai

st.set_page_config(page_title="OpenAI MCP Assistant", layout="centered")
st.title("🧠 OpenAI Assistant (MCP Style)")

question = st.text_area("Ask something (e.g., 'Get info for patient P123')", height=150)
submit = st.button("Ask")

if submit and question.strip():
    with st.spinner("Thinking..."):
        response = call_openai(question)
        st.markdown("### 🤖 OpenAI says:")
        st.success(response)
