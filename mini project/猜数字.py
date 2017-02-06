def Bingo(num1,num2):
    if num1<num2:
        print 'too small'
        return False
    elif num1>num2:
        print 'too big'
        return False
    else :
        print 'that\'s right'
        return True
        
from random import randint
num=randint(1,9999)

print 'guess a number'

bingo=False

while bingo==False:
    answer=input()
    bingo=Bingo(answer,num)