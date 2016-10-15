import urllib
import json

url2 = 'http://python-data.dr-chuck.net/comments_42.json'
url = 'http://python-data.dr-chuck.net/comments_323667.json'

def solution(url) :
	data = urllib.urlopen(url).read()
	datajson = json.loads(data)
	sum = 0
	for item in datajson['comments'] :
		sum += item['count']
	return sum
		
print solution(url)		
print solution(url2)		
