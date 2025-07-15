import streamlit as st
import asyncio
import re

from gemini_client import call_gemini
from mcp_tools import get_patient_info

st.set_page_config(page_title="Gemini vs MCP", layout="centered")
st.title("🧠 Gemini Assistant (MCP Simulated)")

question = st.text_area("Ask a question (e.g., 'Get info for patient P123')", height=150)
submit = st.button("Ask")

# Intent Router
def route_query(text: str):
    match = re.search(r"patient\s*(P\d+)", text, re.IGNORECASE)
    if match:
        return "mcp", match.group(1)
    return "gemini", None

if submit and question.strip():
    with st.spinner("Thinking..."):
        route, patient_id = route_query(question)

        if route == "mcp":
            # Call simulated MCP tool
            response = asyncio.run(get_patient_info(patient_id))
            st.markdown("### 🛠️ MCP Tool Response")
        else:
            # Default to Gemini
            response = call_gemini(question)
            st.markdown("### 🤖 Gemini Response")

        st.success(response)
