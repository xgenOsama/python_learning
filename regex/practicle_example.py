#!/usr/bin/python
import urllib, re

try:
    import urllib.request
except:
    pass

sites = 'google yahoo cnn 123456798 msn'.split(' ')
pat = re.compile(r'<title>+.*</title>*', re.I|re.M)

for s in sites:
    print('Searching : ' + s)
    try:
        u = urllib.urlopen('http://' + s + '.com')
    except:
        u = urllib.request.urlopen('http://' + s + '.com')
    text = u.read()
    title = re.findall(pat, str(text))
    print(title[0])