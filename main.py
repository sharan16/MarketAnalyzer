import json
from sentiment_analyzer import Sentiment_analyzer as s
import requests
import praw

text = "Good movie"
# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.post("http://text-processing.com/api/sentiment/", data = {'text':text})
reddit = praw.Reddit(client_id = 'HrXPcMKV26wpNQ',
					client_secret = '8b1AyC3-CCiD4Cs5TZAKXmYCa-I',
					user_agent = 'my user agent')
for submission in reddit.subreddit('apple').hot(limit=2):
    print(submission.title)

y = json.loads(response.text)
print(y["label"])
