__author__ = 'gen'

import sys
import os
def main():
    print(
    'hello'
    )
    print 'hello i am osama'
    os.system('ls')
    os.system('ping google.com ')
    persons = [{'name': 'osama', 'age': 13}, {'name': 'mohamed', 'age': 16}]
    print(persons[0]['name'])
    print(persons[0]['age'])
    print(persons[1]['name'])
    print(persons[1]['age'])


if __name__ == '__main__':
    main()

