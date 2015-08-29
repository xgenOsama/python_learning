__author__ = 'gen'


family = ['mama', 'ahmed', 'mai', 'osama']

print(family[3])
print(family[-1])


example = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(example[4:8])
print(example[4:10])
# [5, 6, 7, 8]
# [5, 6, 7, 8, 9, 10]

print(example[-5:0])
# []
print(example[-5:])
# [5, 6, 7, 8, 9]
print(example[:7])
# [0, 1, 3, 4, 5, 6, 7]
print(example[:])
# [0, 1, 3, 4, 5, 6, 7, 8, 9]
print(example[1:8:2])
# [1, 3, 5, 7]
print(example[10:0:-2])
# [9, 7, 5, 3, 1]
print(example[::-2])
# [9, 7, 5, 3, 1]

example2 = [10, 30]
print(example + example2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30]

example3 = ['osama', 'mohamed']

print(example2 + example3)
# [10, 30, 'osama', 'mohamed']


print(example3[0] * 10)
# osamaosamaosamaosamaosamaosamaosamaosamaosamaosama

print([21] * 10)

# [21, 21, 21, 21, 21, 21, 21, 21, 21, 21]

name = 'ahmed'

print('z' in name)
# False
print('a' in name)
# True

family2 = ['mom', 'dad', 'bro']

print('mom' in family2)
# True
print('sis' in family2)
# False






