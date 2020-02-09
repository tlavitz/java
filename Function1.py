# 1 Recieve and Return
#prameters and return values

def display(message):
    print(message)

def giveMeFive():
    five=5
    return five

def yesNo(question):
    response=""
    response=None
    while response not in ("y","n"):
        response=input(question).lower()
    return response

#main
display("heres my message")

number=giveMeFive()
print("heres the give me five",number)

answer=yesNo("you think its true? ")
print(answer)
if answer=="n":
    print("why not?")
else:
    print("Lets Play")

#Encapsulation
#No variable you create in a function including parameters,
#can be directly accessed outside its function.

#Abstraction saves you from worrying about the details
#Encapsulation hides details from you

# 2 Demonstrate keyword arguments and default parameter values

#positional parameters
def greet(name,age):
    print("Hi, my name is",name,"and im",age,"years old")
greet("eric",28)

#parameters with default value
#once you assign default values, you have to assign default values to all the parameters
def greet(name="guest",age="1"):
    print("Hi, my name is",name,"and im",age,"years old")

