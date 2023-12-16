def chisla(x,y): 
    if x>99 and x<1000 and y>99 and y<1000:
        x1 = str(x)
        y1=str(y)
        if x1[0]==y1[0] or x1[1]==y1[1] or x1[2]==y1[2]:
            print('совпадают')
        else:
            print('не совпадают')
       
    else:
        print('не правильно')
    
chisla(200,340)
