import re 

# \s space charcter * any number of them () group them



print (re.split(r'(\s*)','here is some words'))

# \s space \S not space \d digest \D not digest
# print (re.split(r'([a-f]','adfadfadfbafjkgbjndalsjfadb'))


print (re.findall(r'\w{1,60}\@\w{1,20}\.\w{1,6}','osama@gmail.com'))


pat = re.findall(r'\w{1,60}\@\w{1,20}\.\w{1,6}','osama@@gmail.com')






if pat:
    print 'this is a true email'
else:
    print 'this is a fake email'
