# display menu
# display task-list
# add task
# del task
# mark as finished

task_list=[]

def dispm():
    '''display menu'''
    print("1. Display Task-list")
    print("2. Add [+] Task ")
    print("3. Del [-] Task")
    print("4. Mark as Read")

def dispt():
    '''display task-list'''
    num=0
    for item in task_list:
        task_value=item[0]
        task_stats=item[1]
        num+=num
        print(num,'--',task_value,'--',task_stats)
    

def addt(x):
    '''add task'''
    task_list.append(x)

def delt(x):
    '''del task'''
    task_list.remove(x)

def masf():
    '''masrk as finished'''
    pass
while True:
    dispm()

    x=input("Enter Operator : ")
    chc=int(x)
    if chc==1:
        dispt()
    elif chc==2:
        x=input('Enter the task[+] : ')
        y=False
        task=(x,y)
        addt(task)
    elif chc==3:
        x=input('Enter the task[-] : ') 
        for item in task_list:
            if x==item[0]:
               # task_list.remove[item]  
               y=item[0]
               z=item[1]
               task=(y,z)
               delt(task) 
    
    elif chc==4:
        x=input('Enter the task[msf]: ')
        for item in task_list:
            if x==item[0]:
                y=item[0]
                z=item[1]
                task=(y,z)
                delt(task)
                za=True
                task=(y,za)
                addt(task)




