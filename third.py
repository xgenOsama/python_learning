__author__ = 'gen'


def my_first_function1(x, y, z):
    summation = (x + y) * z
    return summation



def my_first_function2(x, *args):
    print (x)
    for each_param in args:
        print(each_param)
        print(each_param)

print(my_first_function1(2, 4, 6))

my_first_function2('ahmed', 'osama', 'mohamed', 'ahmed')
