__author__ = 'gen'

face = [21, 18, 50]

print face

face.append(45)

print face

apples = ['i', 'love', 'apples', 'apples', 'now']

print apples

apples.count('apples')
# 2
apples.count('bow')
# 1

one = [1, 2, 3]
print one

two = [4, 5, 6]

one.extend(two)

print one
# [1, 2, 3, 4, 5, 6]


say = ['hey', 'now', 'brown', 'cow']

print say

print say.index('brown')
# 2
say.insert(2, 'white')

print say
# ['hey', 'now', 'white', 'brown', 'cow']

print say.pop(1)
# now
print say
# ['hey', 'white', 'brown', 'cow']
say.remove('brown')

print say
# ['hey', 'white', 'cow']
say.reverse()

print say
# ['cow', 'white', 'hey']


sort_nums = [5, 5, 6, 2, 1, 48, 3]

sort_nums.sort()
sort_nums.reverse()

# timestamp.sort(key=lambda x: time.strptime(x, '%Y-%m-%d %H:%M:%S')[0:6],reverse=True)

print sort_nums
# [1, 2, 3, 5, 5, 6, 48]

print sorted('osamamohamed')
# ['a', 'a', 'a', 'd', 'e', 'h', 'm', 'm', 'm', 'o', 'o', 's']

