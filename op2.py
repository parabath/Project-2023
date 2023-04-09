for i in range(1,5):

    value=input("enter a number")
    gv=float(value)
    count=0
    total_value=0

    if gv>0 or gv<100 :
        count += 1
        total_value += gv
    if gv < 20:
        print("version 1")
    elif gv < 30:
        print("version 2")
    elif gv < 40:
        print("Version 3")
    elif gv < 50:
        print("beta-Version") 
    else:
        print("alfa-version")   

    if count == 5:
        user_choice=input("are you know ALFA & BETA versions (Y/N)")
        if user_choice=="Y":
            print("BETA- developing versions it`s not for industrial usage     ALFA-unstable versions of product.")
            continue




 

