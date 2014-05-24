import urllib2, urllib
def addGETdata(url, data):
	''' tuple type like (key, value)combination 
		((key1, value1),(key2, value2)) or [(,),(,)]
	'''
	return url + '?' urllib.urlencode(data)
