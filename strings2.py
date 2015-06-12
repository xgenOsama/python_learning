__author__ = 'gen'

bucky = 'Hey there %s , hows your %s'


# it's an array
varb = ('betty', 'foot')

print bucky % varb

for v in varb:
    print v

varc = ('tuna', 'fin')

print bucky % varc
# Hey there tuna , hows your fin

example = 'my name is osama'


print example.find('name')
# 3
print example.find('is')

sequence = ['hey', 'there', 'bessie', 'hoss']

print sequence

glue = 'hoss'

glue.join(sequence)

randstr = 'I Wish i had No sausage'

print(randstr)

randstr.lower()

print(randstr)

truth = 'i love old women'

print truth

print truth.replace('women', 'men')

print(truth)

# i love old women
# i love old men
# i love old women


