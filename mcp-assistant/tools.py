from mcp.server.fastmcp import FastMCP
from typing import Optional

mcp = FastMCP("patients")

@mcp.tool()
async def get_patient_info(patient_id: Optional[str] = None) -> str:
    """
    Returns mock patient info by ID.
    """
    if not patient_id:
        return "Patient ID is required."

    mock_db = {
        "P123": "Name: John Doe, Age: 30, Diagnosis: Hypertension",
        "P456": "Name: Jane Smith, Age: 40, Diagnosis: Diabetes"
    }

    return mock_db.get(patient_id, "No patient found with that ID.")
