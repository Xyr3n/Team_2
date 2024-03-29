from dotenv import load_dotenv
import os
import base64
from requests import post
from requests import get
load_dotenv()
client_id = os.getenv("client")
client_secret = os.getenv("secret")

print(client_id)
#code to get access token
def get_token():
    auth_string = client_id + ":" + client_secret

    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')
    url = "https://accounts.spotify.com/api/token"
    headers = {

        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }


    response = post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Failed to retrieve token")
        print("statuscode", response.status_code)
        return None
token = get_token()
print(token)

#get request function
def spotify(endpoint, token):

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = get(f"https://api.spotify.com/v1{endpoint}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("nope")
        return None
data = spotify("/tracks/3Yub3anoLj8w58TVpEXUJv",token)
print(data)
