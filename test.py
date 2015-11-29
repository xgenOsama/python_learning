import urllib
import htmllib
import formatter

website = urllib.urlopen('http://www.google.com')
data = website.read()
website.close()

format = formatter.AbstractFormatter(formatter.NullWritter())
ptext = htmllib.HtmlParser(format)
ptext.feed(data)

for line in ptext.anchorlist:
    print line

ptext.close()
