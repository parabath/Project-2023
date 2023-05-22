# show the menu
# show task list
# add task
# delete task

task_list=[]

def showm():
    # showm() show the menu
    print('1 : show the menu.')
    print('2 : show the task-list.')
    print('3 : add  the task.')
    print('4 : delete a task.')

def showt():
    # showt() show the task list
    nom=1
    for item in task_list:
        value=item[0]
        status=item[1]
        print(nom,'|',value,'|',status)
        nom=nom+1

def addtask(x):
    # addtask() add the task
    task_list.append(x)

def deletask(x):
    # deltask() delete the task
    for i in task_list:
        #a=i[0]
        if x==i[0]:
            a=i[0]
            b=i[1]
            c=(a,b)

            task_list.remove(c) 
        else:
            print('No Data Found!')    

while True:
    showm()
    y=input('Enter the number : ') 
    choice=int(y)
    if choice==1:
        showm()
    elif choice==2:
        showt()  
    elif choice==3:
        x=input('Add a task : ')
        status=False
        taskpack=(x,status)
        addtask(taskpack)
        print('Task was Added!')
    elif choice==4:
        z=input('Delete a task : ')
        deletask(z)
        print('Task was Deleted!')    

