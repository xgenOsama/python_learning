__author__ = 'gen'

class parentClass:
    var1 = 'i\'m var1'
    var2 = 'i\'m var2'

class childClass(parentClass):
    pass

parentObject = parentClass()
print parentObject.var1

childObject = childClass()
childObject.var1 = 'osama'
print childObject.var1

print childObject.var2
print parentObject.var2
print parentObject.var1
print childObject.var1

# i'm var1
# osama
# i'm var2
# i'm var2
# i'm var1
# osama
