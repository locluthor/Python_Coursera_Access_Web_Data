from BeautifulSoup import *
import urllib


url = 'http://chiasenhac.vn/nghe-album/above-and-beyond~audiomachine~ts377mt3qtt8fw.html'
# url1 = 'http://python-data.dr-chuck.net/comments_42.html'
url2 = 'http://python-data.dr-chuck.net/comments_323666.html'

def SumDataOnUrl(url, inputTag):

	sum = 0
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	#Retrieve all of the inputTag tags
	tags = soup(inputTag)
	for tag in tags:
		 sum = sum  + (int)(tag.contents[0])
	return sum	
	
# print SumDataOnUrl(url1, 'span')
print SumDataOnUrl(url2, 'span')