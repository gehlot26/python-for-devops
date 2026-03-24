#program
from dotenv import load_dotenv
load_dotenv()

import os
import requests
from requests.auth import HTTPBasicAuth
import json
email = os.getenv("JIRA_EMAIL")
api_token = os.getenv("JIRA_API_TOKEN")

auth = HTTPBasicAuth(email, api_token)

url = "https://kd26.atlassian.net/rest/api/3/issue"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps({
    "fields": {
        "project": {
            "key": "PROJ"
        },
        "summary": "Test issue from Python",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "This issue is created using API"
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Task"
        }
    }
})

response = requests.post(url, data=payload, headers=headers, auth=auth)

print(response.status_code)
print(response.text)