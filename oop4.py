__author__ = 'gen'

class parent:
    var1 = 'osama'
    var2 = 'mohamed'

class child(parent):
    var2 = 'ebrahem'


pob = parent()
cob = child()

print pob.var1
print pob.var2
print cob.var1
print cob.var2