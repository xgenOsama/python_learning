__author__ = 'gen'

# it's like json objects
book = {'name': 'osama', 'age': 13, 'wife': 'bob'}

print book

print book['name']
print book['age']

ages = {'dad': '42', 'mom': '87'}

print ages
print ages['dad']


book.clear()
print book

tuna = ages.copy()
print tuna

tuna['dad'] = 30

print tuna
print ages

print tuna.has_key('mom')

print tuna.has_key('osama')

# {'age': 13, 'name': 'osama', 'wife': 'bob'}
# osama
# 13
# {'dad': '42', 'mom': '87'}
# 42
# {}
# {'dad': '42', 'mom': '87'}
# {'dad': 30, 'mom': '87'}
# {'dad': '42', 'mom': '87'}
# True
# False
