import sys


def box_print(symbol,height,width):
    if len(symbol) != 1 :
        raise Exception('The length of symbol is not 1')
    if width<=2 :
        raise Exception('The width is less than 2')
    if height<=2 :
        raise Exception('The height is less than 2')
    print (symbol * width)
    for i in range (height-2):
        print (symbol +(' ' * (width-2))+symbol)
    print(symbol * width)

def box_print1 (symbol1,symbol2,height,width):
    print(symbol1 * width)
    for i in range (height-2) :
        print(symbol2 +(' ' * (width-2))+symbol2)
    print(symbol1 * width)

try:
    box_print('*',4,4)
    box_print('*', 4, 10)
    box_print('x', 1, 10)
except Exception as err :
    print('An exception happened: '+str(err))

try:
    box_print1('-','|',5,10)
except Exception as err :
    print('An exception happened.'+str(err))

ages = [16,10,13,4,50,25,17]
ages.sort()
print(ages)
assert ages[0]<=ages[-1]
print('assert 1 success')
assert ages[0]>=ages[-1]
print('assert 2 success')
