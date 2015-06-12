__author__ = 'gen'


def whatsup(x):
    return 'whats up ' + x

print whatsup('osama')

def plusten(y):
    return y + 10

print plusten(1)

def name(first, last):
    print '%s %s' % (first, last)


name('bucky', 'reberts')

def name1(first='osama', last='moahmed'):
    print '%s %s' % (first, last)


name1('ahemd')

name1(last='ebrahem')


def list(*food):
    print food

list('apples')
list('apples', 'peaches', 'beef')

def profile(name, *age):
    print name
    print age


profile('osama', 42, 3, 5, 6)

def cart(**items):
    print items

cart(apples=5, peaches=6, beef=60)

def profile(first, last, *ages, **items):
    print first, last
    print ages
    print items

profile('osama', 'mohamed', 42, 3, 5, 6, bacon=4, saus=64)




def example(a, b, c):
    return a + b * c

tuna = (5, 7, 3)
print example(*tuna)

def example2(**this):
    print this

bacon = {'mom': 32, 'dad': 54}

example2(**bacon)


