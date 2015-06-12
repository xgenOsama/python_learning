__author__ = 'gen'


# fob = open('test.txt','w')
# print fob.writable()
# fob.write('hello i am an engineer')
# fob.close()

# fob = open('test.txt', 'r')
# print fob.readline()
# print fob.readline()
# fob.close()

# fob = open('test.txt', 'a')
# fob.write('\ng33k here')
# fob.close()

fob = open('test.txt', 'r')
listLines = fob.readlines()

print listLines
fob.close()