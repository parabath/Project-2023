"""
PS OPERATING SYSTEM
"""

def total(x):
    """Define the Total"""
    total=0
    for i in x:
        #total=total+i
        '''total +=i'''
        '''total=total+i'''
        total+=i
        #return total
    return total   

'''def total(x):
    total = 0
    for i in x:
        total += i
    return total'''

def max(x):
    """Define the Max"""
    max=0
    #if max==0:
        #max='0 or No.Digit.Found' 
    for i in x:
        if i >max:
            max=i   
        else:
            #max='No Digit Found'
            max=max
    return max  

def min(x):
    """Define the Min"""
    #min=0
    #if min==0:
        #min='0 or No.Digit.Found'

    for i in x:
        min=i
        if i<min:
            min=i  
        return min                

    
def sq(b,p):
    #sqr=b*pow(b*(p-1))
    sqr=b*pow(b,(p-1))
    return sqr

