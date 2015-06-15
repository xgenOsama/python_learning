__author__ = 'gen'

import sys
import os
import thread
import datetime
def main():
    print(
    'hello'
    )
    print 'hello i am osama'
    os.system('ls')
    os.system('ping google.com -c 3')
    persons = [{'name': 'osama', 'age': 13}, {'name': 'mohamed', 'age': 16}]
    print(persons[0]['name'])
    print(persons[0]['age'])
    print(persons[1]['name'])
    print(persons[1]['age'])
    persons.insert(2, {'name': 'ahmed', 'age': 11})
    for s in persons:
        print(s)
    print(persons[0]. has_key('name'))
    print(persons[0].viewkeys())
    print(persons[0].items())
    cop = persons[0].copy()
    persons[0] = None
    print(cop)
    mythread = thread
    def printDate():
        print(datetime.date.today())

    printDate()


if __name__ == '__main__':
    main()

