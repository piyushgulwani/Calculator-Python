import math

def add():
    a = int(input("Enter number1:  "))
    b = int(input("Enter number2:  "))
    print(a+b)


def sub():
    a = float(input("Enter number1:  "))
    b = float(input("Enter number2:  "))
    print(a-b)

def modulos():
    a = float(input("Enter no 1:  "))
    b = float(input("Enter no 2:  "))
    print(a//b)
    
    
def mul():
    a = float(input("Enter number1:  "))
    b = float(input("Enter number2:  "))
    print(a*b)
    

def divide():
    a = float(input("Enter number1:  "))
    b = float(input("Enter number2:  "))
    print(a/b)

def root():
    a = float(input("Enter a number1: "))
    print(math.sqrt(a))
    
    
def square():
    a = float(input("Enter a number1: "))
    print(a*a)
    
    
while True: 
    print("<1> Add <2> Sub <3> Mul <4> Divide <5> Root <6> Square <7> Modulus <8> Quit")
    
    cal = int(input(""))
    
    if cal == 1:
        add()
        
    elif cal == 2 :
        sub()
        
    elif cal == 3:
        mul()
        
    elif cal == 4:
        divide()
        
    elif cal == 5 :
        root()
        
    elif cal == 6:
        square()
        
    elif cal == 7 : 
        modulos()
        
    elif cal == 8 :
        break
    
    else :
        print("Invalid Input")