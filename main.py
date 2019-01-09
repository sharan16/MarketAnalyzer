import json
import requests

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.post("http://text-processing.com/api/sentiment/", data = {'text':'good movies'})

print(response.json())