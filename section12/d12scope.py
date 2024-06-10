#c1#global variables
name = 'riyaz'

def namefunction():
    
    print(f'name inside function: {name}')
    return name

newname = namefunction()
print(f'name outside function: {newname}')

#c2#global variables
i=50
def foo():
    i=100
    return i

foo()
print(i)