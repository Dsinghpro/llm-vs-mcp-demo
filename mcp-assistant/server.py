from mcp.server.fastmcp import FastMCP
from typing import Optional
from openai_client import call_openai

mcp = FastMCP("assistant")

@mcp.tool()
async def get_patient_info(patient_id: Optional[str] = None) -> str:
    if not patient_id:
        return "Please provide a valid patient ID."
    
    # Mocked data
    if patient_id == "P123":
        return "Patient: John Doe, Age: 45, Gender: Male, Conditions: Diabetes, Hypertension."
    else:
        return f"No patient found with ID {patient_id}."

@mcp.tool()
async def ask_openai(question: str) -> str:
    return call_openai(question)

if __name__ == "__main__":
    print("🚀 MCP server with OpenAI started.")
    mcp.run(transport='stdio')
