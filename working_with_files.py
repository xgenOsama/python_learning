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

# fob = open('test.txt', 'r')
# listLines = fob.readlines()
#
# print listLines
#
# listLines[2] = '\n i\'m g33k'
#
# print listLines
fob = open('test.txt', 'w')
write = ['\nosama', '\nabdo']
fob.writelines(write)
# listLines2 = fob.readlines()
# print listLines2
fob.close()

