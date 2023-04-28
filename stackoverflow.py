import requests

# Define the API endpoint URL and parameters
url = "https://api.stackexchange.com/2.3/search"
params = {
    "site": "stackoverflow",
    "intitle": "bpm",
    "order": "desc",
    "sort": "votes"
}

# Send the GET request to the API and get the response
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Get the first question from the response
    question = response.json()["items"][0]
    print("Title:", question["title"])
    print("Link:", question["link"])
else:
    print("Error:", response.status_code)