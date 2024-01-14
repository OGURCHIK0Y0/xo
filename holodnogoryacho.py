import random as r
def num():
    while 1:
        num= r.randint(100,999)
        if str(num)[0]!=str(num)[1] and str(num)[1]!=str(num)[2] and str(num)[0]!=str(num)[2]:
            return num
        
    
s=num()
def chek(a,b):
    if a==b:
        print('красафчк')
        return 1
    elif str(a)[0]==str(b)[0] or str(a)[1]==str(b)[1] or str(a)[2]==str(b)[2]:
        print("горяч")
    elif str(b)[0] in str(a) or str(b)[1]  in str (a) or str(b)[2] in str (a):
        print("тепло")
    else:
        print("холодно")
print(s)
t=int(input('введите число'))
while 1:
    chek(s,t)
    t=int(input('введите число'))
