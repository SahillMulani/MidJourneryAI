import requests
import json

# Take user input
user_input = input("Please enter your input: ")

# Set up API request to Midjournery AI
url = "https://api.midjourney.com/template/generate"
payload = {"input": user_input}
headers = {"Content-Type": "application/json"}

# Send API request and get response
response = requests.post(url, data=json.dumps(payload), headers=headers)

# Save response as a file
with open("template.docx", "wb") as file:
    file.write(response.content)
