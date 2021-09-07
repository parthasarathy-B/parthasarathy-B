
data=[
    {

        'question':'A) which is the king of jungle ?',
        'options':['1) Zebra','2) eliphant','3) Tiger','4) Lion'],
        'ans':4
    },
    {
        'question':'B) what is the capital of india ?',
        'options':['1) Chennai','2) Dheli','3) Mumbai','4) Kerala'],
        'ans':2
    },
    {

        'question':'C) which is our national animal ?',
        'options':['1) Tiger','2) Lion','3) Zebra','4) Elephant'],
        'ans':1
    }
    ]


s=int(input('Enter the number of students :'))
print('')
print('--------------------------------------------------------------------------------------------------------------------------------')

for k in range(1,s+1):
    print('STUDENT',k)
    reg=int(28850+k)
    print('REGISTER NO :',reg)
    r=int(input('Enter your register number :'))
    if (r==reg):
        pass
    else:
        print('! enter the correct register number!')
        break
    print('')
    right=0
    wrong=0

    for i in data:
        print(i['question'])
        for j in i['options']:
            print(j)
        ans=int(input('Enter the answer :'))
        if (ans==i['ans']):
            right+=1
        else:
            wrong+=1
        print('')
    total=(right+wrong)
    percentage= (right/total)*100

    print('****************************************')
    print('RESULT OF STUDENT -',k,'|  REG NO :',reg)
    print('****************************************')
    print('| Total marks :',total)
    print('| Right :',right)
    print('| Wrong :',wrong)
    print('| PERCENTAGE :',int(percentage),'%')
    print('****************************************')
    print('')
    print('--------------------------------------------------------------------------------------------------------------------------------')
