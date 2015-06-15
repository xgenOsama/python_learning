__author__ = 'gen'

import sys
import os
import thread
import datetime
import time
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

    def print_time(threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print "%s: %s" % (threadName, time.ctime(time.time()))

    # Create two threads as follows
    try:
       mythread.start_new_thread(print_time, ("Thread-1", 2, ))
       mythread.start_new_thread(print_time, ("Thread-2", 4, ))
    except:
       print "Error: unable to start thread"

    while 1:
       pass
if __name__ == '__main__':
    main()

