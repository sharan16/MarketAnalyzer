import json
import requests
class Sentiment_analyzer:
	def __init__(self):
		self.pos = 0
		self.neg = 0
		self.neut = 0
		self.item_count = 0
		print("class created")
	
	def classify(self, text):
		response = requests.post("http://text-processing.com/api/sentiment/", data = {'text':text})
		print(response.text)
		self.pos += response.json()["probability"]["pos"]
		self.neg += response.json()["probability"]["neg"]
		self.neut += response.json()["probability"]["neutral"]
		self.item_count+=1
		print(str(self.pos) + ', ' + str(self.neut) + ', ' + str(self.neg))
		return [self.pos, self.neut, self.neg]
	
	def average(self):
		return [self.pos/self.item_count, self.neut/self.item_count, self.neg/self.item_count]
	
	def evaluate(self):
		average = self.average()
		return average.index(max(average))

		
'''
s = Sentiment_analyzer()
array = s.classify("good")
print(s.evaluate())
'''