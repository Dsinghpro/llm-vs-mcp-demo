from typing import Optional

async def get_patient_info(patient_id: Optional[str] = None) -> str:
    mock_db = {
        "P123": "Name: John Doe, Age: 30, Diagnosis: Hypertension",
        "P456": "Name: Jane Smith, Age: 40, Diagnosis: Diabetes"
    }

    if not patient_id:
        return "Patient ID is required."

    return mock_db.get(patient_id, f"No patient found with ID {patient_id}.")
