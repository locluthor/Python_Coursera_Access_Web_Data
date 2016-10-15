import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
url2 = 'http://python-data.dr-chuck.net/known_by_Aleksandar.html '

def findlink(url, position) :
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	tags = soup('a')

	links = []

	for tag in tags :
		links.append(tag.get('href', None))
		# print tag.get('href', None)
		
	return links[position - 1]

def listall(url, count , position) :

	links = []

	for i in range(count) :
		newurl = findlink(url, position)
		links.append(newurl)
		print newurl
		url = newurl

listall(url2, 7, 18)
	
# print links