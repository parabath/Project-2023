def gcalc(n:float)->str:
    if 0>n>100:
        print('invalid')
        return n
    elif 0>=n<35:
        print('grade f')
        return n
    elif 35<=n<55:
        print('grade s')
        return n
    elif 55<=n<65:
        print('grade c')
        return n
    elif 65<=n<75:
        print('grade B')
        return n
    elif 75<=n<=100:
        print('grade A')
        return n
    else:
        print('Invalid 0xxn')
        return n    
    
count=0
total=0
for i in range(0,6):
    x=input('Enter a valid mark')
    marks=float(x)
    count+=1    
    total+=marks
    gcalc(marks)
    avm=total/count
    print(avm)

    y=input('Continue Y|N')
    if y=='N':
        break
    
    
