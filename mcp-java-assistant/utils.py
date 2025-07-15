import json
import requests

def unwrap_mcp_response(url):
    try:
        res = requests.get(url)
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def count_clients_in_context(context_json: str) -> int:
    try:
        data = json.loads(context_json)
        if isinstance(data, list):
            return len(data)
        elif isinstance(data, dict) and "clients" in data:
            return len(data["clients"])
        return 0
    except Exception as e:
        print("❌ Error parsing context:", e)
        return 0

def trim_clients(context_json: str, max_clients: int = 15) -> str:
    try:
        data = json.loads(context_json)
        if isinstance(data, list):
            return json.dumps(data[:max_clients], indent=2)
        return context_json
    except Exception as e:
        print("❌ Error trimming clients:", e)
        return context_json
