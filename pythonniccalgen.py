import datetime

x=input('Enter nic')
if 12 != len(x):
    print('check your nic again!')
else :
   #isdigit=x.is_digit()
   print('Generating...')

def byear(y:int)->int:
    #year=y[0:4]
    #return year
    #return y[0:4]
    year=y[0:4]
    return year

def bday(y:int)->int:
    #day=y[4:7]
    #return day
    #return y[4:7]
    day=y[4:7]
    cday=int(day)
    if cday>500:
        day=cday-500
        gen='Female'
        
    else:
        gen='male'  
        
    print(gen)   
    return day

def dte(y:int)->int:
    yr=int(byear(x))
    da=int(bday(x))
    jan_f=datetime.date(yr,1,1)
    cdte=jan_f+datetime.timedelta(da-1)
    return cdte

    



birthy=byear(x)
birthd=bday(x)
gendate=dte(x)

print(birthy)
print(birthd)
print(gendate)



