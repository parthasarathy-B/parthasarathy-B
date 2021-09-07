import random
import sys


def roll():
    a=(random.randint(0,3))
    b=(random.randint(0,3))
    print('[',a,']','   ''[',b,']')
    c=(a+b)
    print(' ')
    if c==0:
        c=12
    print('    ','(',c,')')
    print(' ')
    
    if c==1 or c==5 or c==6 or c==12:
        print('Role the dice again')
    else:
    
        print('''You lose
========================================''')               
                   

while True:
    inp=input('          ')
    if inp==(''):
        roll()
    else:
        sys.exit()





