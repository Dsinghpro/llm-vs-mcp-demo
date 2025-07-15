import streamlit as st
import json
from gemini_handler import query_model
from utils import unwrap_mcp_response, count_clients_in_context, trim_clients

st.title("🧠 MCP Client Explorer with Gemini")

# Call your Flask MCP proxy endpoint
api_url = "http://localhost:5000/mcp/clients"
response = unwrap_mcp_response(api_url)
client_data = response.get("mcpBody", [])

# Show raw data (optional)
with st.expander("📄 View Raw Client JSON"):
    st.json(client_data)

# Ask a question
question = st.text_input("Ask a question about the clients:")

if question:
    if len(client_data) > 0:
        # Trim and convert to JSON string for Gemini
        context_str = json.dumps(client_data[:15])  # Limit to 15 clients
        answer = query_model(context_str, question)

        st.markdown("### 🤖 Gemini Answer")
        st.success(answer)
    else:
        st.warning("No client data found to analyze.")
