"""LambdaTest API Metadata Class"""

import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env", override=True)

username = os.getenv("LT_USERNAME")
access_key = os.getenv("LT_ACCESS_KEY")

class APImetadata:

    # fetch builds metadata from LambdaTest API
    def fetch_builds_data(self):
        url = "https://api.lambdatest.com/automation/api/v1/builds?limit=5"
        auth = (username, access_key)

        response = requests.get(url=url, auth=auth)
        if response.status_code == 200:
            builds_data = response.json()
            print("<====== BUILDS DATA ======>")
            print(builds_data)
            return builds_data
        else:
            print("Failed to fetch builds. Status code:", response.status_code)
            print("Error Message:", response.text)
            return None

    # fetch sessions metadata from LambdaTest API
    def fetch_sessions_data(self):
        url = "https://api.lambdatest.com/automation/api/v1/sessions?limit=2"
        auth = (username, access_key)

        response = requests.get(url=url, auth=auth)
        if response.status_code == 200:
            sessions_data = response.json()
            print("<====== SESSIONS DATA ======>")
            print(sessions_data)
            return sessions_data
        else:
            print("Failed to fetch sessions. Status code:", response.status_code)
            print("Error Message:", response.text)
            return None
