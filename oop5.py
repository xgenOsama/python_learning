__author__ = 'gen'


class Mom:
    var1 = 'hey i\'m mom'

class Dad:
    var2 = 'hey there son i\'m adad'

class child(Mom,Dad):
    var3 = 'i\'m new varibale'


childobject=child()

print childobject.var1
print childobject.var2
print childobject.var3