import htmllib, urllib, sys, formatter

website = urllib.urlopen('http://www.google.com')
data = website.read()
website.close()

format = formatter.AbstractFormatter(formatter.DumbWriter(sys.stdout))
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
ptext.close()

