import urllib
import xml.etree.ElementTree as ET

xmlurl = 'http://python-data.dr-chuck.net/comments_42.xml'
xmlurl2 = 'http://python-data.dr-chuck.net/comments_323663.xml'


def ParseXml(url) :
	data = urllib.urlopen(url).read()
	# print data
	tree = ET.fromstring(data)
	# print tree
	comments = tree.findall('comments/comment')
	sumcount = 0
	# print len(comments)
	for comment in comments :
		sumcount += int(comment.find('count').text)
		# print 'sumcount = ', sumcount
	return sumcount

def ParseXml2(url) :
	data = urllib.urlopen(url).read()
	# print data
	tree = ET.fromstring(data)
	# print tree
	comments = tree.findall('.//count')
	sumcount = 0
	# print len(comments)
	for comment in comments :
		sumcount += int(comment.text)
		# print 'sumcount = ', sumcount
	return sumcount	
	
print ParseXml(xmlurl)
print ParseXml2(xmlurl2)