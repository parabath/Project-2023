import datetime

x=input('Enter your identiticard-number : ')

borny=x[0:4]
borndc=x[4:7]

def calculate_bod(x:int,y:int):
    jan_f=datetime.date(x,1,1)
    #b_da=datetime.date(y)+datetime.deltatime(jan_f-1)
    #b_da=jan_f+datetime.deltatime(y-1)
    if y>500:
        y=y-500
        gender='Female'
        print('Gen : ',gender)
       
    else:
        y=y
        gender='male'    
        print('Gen       : ',gender)
    
    b_da=jan_f+datetime.timedelta(y-1)
    return b_da

a=int(borny)
b=int(borndc)
z=calculate_bod(a,b)
print('Birth_Day : ',z)