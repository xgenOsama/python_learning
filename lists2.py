__author__ = 'gen'


numbers = [8, 1, 4, 17, 28, 165, 7]

print len(numbers)
print max(numbers)
print min(numbers)


chars = list('bucky')

for char in chars:
    print char

# 7
# 165
# 1
# b
# u
# c
# k
# y


numbers[0] = 33

print(numbers)
# [33, 1, 4, 17, 28, 165, 7]

numbers2 = numbers

numbers2[0] = 22

print(numbers2)
# [22, 1, 4, 17, 28, 165, 7]

print(numbers)
# [22, 1, 4, 17, 28, 165, 7]

del numbers2[0]

print(numbers2[0])

# 1

example = list('easyhoss')

print example
# ['e', 'a', 's', 'y', 'h', 'o', 's', 's']
example[4:] = list('baby')

print example
# ['e', 'a', 's', 'y', 'b', 'a', 'b', 'y']
example[4:] = list('racecars')

print example
# ['e', 'a', 's', 'y', 'r', 'a', 'c', 'e', 'c', 'a', 'r', 's']

example = [7, 8, 9]

print example
# [7, 8, 9]
example[1:1] = [3, 3, 3]

print example
# [7, 3, 3, 3, 8, 9]

example[1:5] = []

print example
# [7, 9]


