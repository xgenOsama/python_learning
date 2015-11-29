import urllib,htmllib,formatter,re,sys

url = sys.argv[1]

website = urllib.urlopen('http://'+url)
data = website.read()
website.close()

format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
links = []
links = ptext.anchorlist
counter = 0 
for link in links:
    if re.search('http', link) != None:
        print str(counter) + " : " + link
        counter += 1
        website = urllib.urlopen(link)
#        data = website.read()
        website.close()
        ptext = htmllib.HTMLParser(format)
        ptext.feed(data)
        morelinks = ptext.anchorlist
        for alink in morelinks:
            if re.search('http', alink) != None:
                links.append(alink)
