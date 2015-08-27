import urllib

myurl = urllib.urlopen('http://www.google.com')
contents = myurl.readlines()
'i am engineer from hell'
# print(contents[0][-1:len(contents[0])/2:-1])

headerInfo = myurl.info()

print(headerInfo)
print(headerInfo.getheader('content-type'))
print(headerInfo.getheader('date'))


urllib.urlretrieve('http://www.google.com' , 'googleContent')
