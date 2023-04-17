import datetime

def nicagru(x):
   return len(x)

def borny(x):
   return x[0:4]

def bornd(x)->datetime.date:
   return x[5:7]

y=input("ID NO : ")
result=nicagru(y)
print(result)

if(result!=12):
   print('Enter a valid ID')
else:
   print('Processing') 
   bornyear=borny(y) 
   print(bornyear)

if(result==12):
   bornday=int(bornd(y))
   jan_first=(bornyear,1,1)
   born_date=jan_first + datetime.timedelta(days=bornday-1)
   print(born_date)
else:
   print("Error!")   
  

