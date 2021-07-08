#Add implementation
def add(x,y):
    return x+y
#Subtract implementation
def subtract(x,y):
    return x-y   #on master branch
#Multiply implementation
def multiply(x,y):
    return x*y    #on bug456 branch
#Divide implementation
def divide(x,y):  #on bug786 branch
    if y==0:
        return DIVIDE_BY_0_ERROR
    else:
        return x/y
#square implementation
def square(x,y):
    pass
