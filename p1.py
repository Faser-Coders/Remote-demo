#without arguments and without return
def fun1():
    print("Function without arguments and without return type")
    a=10
    b=20
    c=a+b
    print("Sum of",c)
    
fun1()

#with arguments and without return
def fun2(x,y):
    print("Function with aruguments and without return")
    a=x
    b=y
    c=a+b
    print("Sum of",c)
    
fun2(11,22)

#without arguments and with return type
def fun3():
    print("Function without arguments and with return")
    a=10.50
    b=20
    c=a+b
    return c
print("Sum =",fun3())

#with aruguments and with return
def fun4(x,y):
    print("Function with aruguments and with return")
    a=x
    b=y
    c=a+b
    return c
print("Sum of x and y is",fun4(10,20))
