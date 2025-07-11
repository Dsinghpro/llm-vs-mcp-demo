import streamlit as st
import asyncio
from together_client import call_together_llm

st.set_page_config(page_title="Together AI MCP Assistant", layout="centered")
st.title("🧠 Together AI Assistant (MCP Enabled)")

question = st.text_area("Ask something...", height=150)
submit = st.button("Ask Together AI")

if submit and question.strip():
    with st.spinner("Thinking..."):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            response = loop.run_until_complete(call_together_llm(question))
            st.markdown("### 🤖 Together AI says:")
            st.success(response)
        except Exception as e:
            st.error(f"❌ Error: {e}")
