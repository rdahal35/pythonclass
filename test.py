x = 6

def example():
    print(x)
    # z, however, is a local variable.  
    z = 5
    # this works
    print(z)
    
example()
print('------------------------')

x=6
def example2():
    # works
    print(x)
    print(x+5)

    # but then what happens when we go to modify:
    x+=6

example2()

print('-----------------------------')

x=6
def example3():
    # what we do here is defined x as a global variable. 
    global x
    # now we can:
    print(x)
    x+=5
    print(x)
example3()

print('-------------------')

x=6
def example4():
    globx = x
    # now we can:
    print(globx)
    globx+=5
    print(globx)

example4()
