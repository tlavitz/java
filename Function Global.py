#Demo for global variables

def global1():
    #value+=20
    print("From global1,value is",value)

def global2():
    value=5
    print("From global2,value is",value)

def global3():
    global value
    value=20
    value+=50
    print("From global3,value is",value)

#main
value=10
print("In global scope, value is",value)

global1()
print(value)
global2()
print(value)
global3()
print(value)