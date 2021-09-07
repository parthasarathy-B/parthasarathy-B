import random

ME=0
BOT=0
a= ['rock  ','scissor','paper ']
b= ['rock  ','scissor','paper ']
ans=('')

print('* Press Enter button to Continue')
print('* Press any other letter and Enter button to Exit')


while(ans==''):
    ans=input('               ')
    if (ans !=''):
        break
    
    bot=(random.choice(a))
    me=(random.choice(b))
    print('Bot :',bot,end='          ')
    print('Me :',me)
    print('            ',end='')
    if ((bot==a[0] and me==b[1])or(bot==a[1] and me==b[2])or(bot==a[2] and me==b[0])):
        BOT+=1
        print('!YOU LOSE!')
    elif(bot==me):
        print('!DRAW!')
    else:
        ME+=1
        print('!YOU WIN!')

print('--------------------------------------------------------------------------------')
print('ME  = ',ME)
print('BOT = ',BOT)

if ME>BOT:
    print('''     ---------------------
     | YOU WON THE MATCH |
     ---------------------''')
elif ME<BOT:
    print('''     ----------------------
     | YOU LOSE THE MATCH |
     ----------------------''')
else:
    print('''     -----------------
     | MATCH IS DRAW |
     -----------------''')
input()

    
