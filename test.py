import base64

clientid = "SCP_TEST2_LOBBY_client_APPID"
client_secret_key = "cf41dce8-adf7-40f7-9afb-700092c219e5"

print(base64.b64encode(f"{clientid}:{client_secret_key}".encode()).decode())