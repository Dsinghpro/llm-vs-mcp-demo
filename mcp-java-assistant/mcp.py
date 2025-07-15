import requests
from config import API_URL, API_KEY, AUTH_TOKEN, CLIENT_ID, CLIENT, USER_ID, USER_NAME

def get_clients_data():
    headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.9",
    "api_key": "402692fc0614418b80fbe1606ebebe12",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlM0VRN1RGd0tUZ3NXYVpxZU56cDNjaHZaWE80bUQ2RllzQ2ZsLUNfdm9NIn0.eyJleHAiOjE3NTI1NjczMTUsImlhdCI6MTc1MjU2MTMxNSwianRpIjoiMjkwNDJiOGQtZWQxOS00YzAzLTljODgtYTNjMWJmYWFkM2QyIiwiaXNzIjoiaHR0cDovLzIwLjEyNy43OC40MDo4MDgwL2F1dGgvcmVhbG1zL1BhaW5TY3JpcHRBcHAiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiZjo5YTY0NGMxZi1lMGIzLTRlZjMtYWQ4Ny1mMGEzZDhmYmZlOGE6MSIsInR5cCI6IkJlYXJlciIsImF6cCI6InBhaW5zY3JpcHQtYWRtaW4tYXBwIiwic2Vzc2lvbl9zdGF0ZSI6ImZjMmViOTJiLTNjMGItNDAzNy1hNDM2LTgxZWYxZTJkMzBmZSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJBZG1pbnMiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJmYzJlYjkyYi0zYzBiLTQwMzctYTQzNi04MWVmMWUyZDMwZmUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJQYWluc2NyaXB0IEFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicHNhZG1pbkBwYWluc2NyaXB0LmNvbSIsImdpdmVuX25hbWUiOiJQYWluc2NyaXB0IiwiZmFtaWx5X25hbWUiOiJBZG1pbiJ9.gFVkBdrFc_Sw7QdL-2Sx-5zEECalXdCN1ihhQcrPm7xreMbe5yuayDTQ7iTWHlNZ1inoKaVML96J1bEnrMES5I5eMkS-UPpeo5iEx2KMvexb5XlKmt1sKH6ngSMRMzebCzPSBK8aMgQU7q2Fm9c3DMnYfanA0t00vxaBK9fCKIqQ4mqUbeHwKGF_Jbs7EIktgl1LNkA-9_lFf1oQzkZMUA7_AazqbaIv_41IIpwq4rB50tqGWdI7ZsMpNObtXJX5X181AjPFpJEjV1021Dqi4p4VdMpjCLiZB79YB6ZaC5_TyOvElLBeqhOzcbRNV0Bdo3iAKkKHOSq6MkAsflKX8g",
    "clientid": "painscript-admin-app",
    "connection": "keep-alive",
    "content-type": "application/json",
    "email": "psadmin@painscript.com",
    "host": "painscript-uat-api-management.azure-api.net",
    "origin": "http://admin-app-painscript-dev.apps.yw8un8hh.eastus.aroapp.io",
    "referer": "http://admin-app-painscript-dev.apps.yw8un8hh.eastus.aroapp.io/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "userid": "1",
    "username": "psadmin@painscript.com"
}
    try:
        response = requests.get(API_URL, headers=headers)
        status = response.status_code
        body = response.json() if response.ok else {"error": response.text}
        return {
            "mcpHeader": {
                "version": "1.0",
                "status": status
            },
            "mcpBody": body
        }, status
    except Exception as e:
        return {"error": str(e)}, 500
