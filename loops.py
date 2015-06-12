__author__ = 'gen'


b = 1

while b <= 10:
    print b
    b += 1

g1 = ['bread', 'milk', 'meat', 'beef']

print g1

for food in g1:
    print 'I want :' +food

ages = {'dad': 42,'mom': 48,'lisa': 7}
print ages

for item in ages:
    print item

for item in ages:
    print item, ages[item]

while 1:
    name = raw_input('Enter name :')
    if name == 'quit':
        break
