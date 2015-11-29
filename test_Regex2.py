import urllib, re


try:
    import urllib.request
except:
    pass

sites = 'google yahoo cnn msn'.split(' ')
pat = re.compile(r'<title>+.*<title>*', re.I|re.M)

for s in sites:
    print ('Searching : '+ s)
    try:
        url = urllib.urlopen('http://'+s+'.com')
    except:
        url = urllib.request.urlopen('http://'+s+'.com')
    text = url.read()
    title = re.findall(pat, str(text))
    print title[0]
