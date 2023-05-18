#display op menu
#1-display list
#2-add task

"""Create the task_list"""
task_list=[]

"""function to show the op menu"""
def display_menu():
    print("---------Menu--------")
    print("1-Display  .task-list")
    print("2-Add-task .task-list")
    print("---------------------")

"""Add task to task-list"""
def add_task(x):
    #x=input("Type the task")
    #task_value=x
    #task_status=False
    #task_pkg=(task_value,task_status)
    task_list.append(x)

"""Display the task-list"""    
def display_list():
    task_no=1
    for i in task_list:
        t_value=i[0]
        t_status=i[1]
        print(task_no,'|',t_value,'|',t_status)
        task_no+=1
    #print(task_no,'|',t_value,'|',t_status)
    
"""User-Control-panel(operating_system!)"""
while True:
    display_menu()
    find=input("Input the operator : ")
    choice=int(find)
    if choice==1:
        display_list()
    elif choice==2:
        y=input('Enter the Task : ')
        task_value=y
        task_status=False
        task_pak=(task_value,task_status)
        add_task(task_pak)
