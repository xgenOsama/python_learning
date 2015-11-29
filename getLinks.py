import urllib,re,sys

symbol = sys.argv[1]

url = 'http://finance.google.com/finance?q='

content = urllib.urlopen(url+symbol).read()
m = re.search('span id="ref.*">(.*)<',content)
if m:
    quote = m.group(1)
else:
    quote = 'no quote or symbol: ' + symbol

print(quote)
