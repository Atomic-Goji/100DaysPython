# This is an advanced calculator 

def add(a,b):
    return print(a+b)

def subtract(a,b):
    return print(a-b)

def multiply(a,b):
    return print(a*b)

def division(a,b):
    return print(a/b)
    
def explonential(a,b):
    return print(a**b)

def floor_division(a,b):
    return print(a//b)

d = int(input("Enter the first number: "))
e = int(input("Enter the second number: "))

print("""CHOOSE YOUR FUNCTION
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      5. Exponential
      6. Floor division
      PLZ WRITE THE CORRESPONDING NUMBER""")

c = input("Enter your choice: ")

if c == "1":
  add(d,e)

if c == "2":
  subtract(d,e)

if c == "3":
  multiply(d,e)

if c == "4":
  division(d,e)

if c == "5":
  explonential(d,e)

if c == "6":
  floor_division(d,e)




