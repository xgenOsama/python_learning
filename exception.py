# try:
#     num = 3/0
#     print num
# except ValueError:
#     print 'can\'t divide into zero'

try:
    number = int(raw_input('Enter a number: '))
    print(number)
    afile = open('not.txt')
    print(afile.readline())
except ValueError:
    print('not a number please try again')
    number = int(raw_input('Enter a number: '))
except IOError:
    print 'can\'t find the file'
print('finished')




