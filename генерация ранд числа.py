import random as r

def num():
    while 1:
        num= r.randint(100,999)
        print(num)
        if str(num)[0]!=str(num)[1] and str(num)[1]!=str(num)[2] and str(num)[0]!=str(num)[2]:
            print('подх')
            print(num)
            break
    
    
num()
