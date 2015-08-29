__author__ = 'gen'


class className:
    def createName(self, name):
        self.name = name

    def displayName(self):
        return self.name

    def saying(self):
        print 'hello %s' % self.name


print className


first = className()
second = className()

first.createName('osama')
second.createName('ahmed')
print first.displayName()
print second.displayName()

first.saying()
second.saying()