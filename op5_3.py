import datetime

def borny(x):
    return(x[0:4])

def bornd(x):
    return(x[4:7])
    

y=input("ENTER ID : ")
byear=int(borny(y))
bday=int(bornd(y))
print(bday)
print(byear)

janf=datetime.date(byear,1,1)
born_date=janf + datetime.timedelta(days=bday-1)
print(born_date)
