import time

x = 3

while True:
 print(x)
 x -=1
 time.sleep(1)                    
if x==0:
    print("lets go")
    break

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def divide(x,y):
    return x / y
def multiply(x,y):
    return x * y

print("lets start our calculator")
print("1=+")
print("2=-")
print("3=÷")
print("4=×")

while True:
    A = input("Enter choice (1/2/3/4) :")
    if A in ("1","2","3","4"):
        try:
           num1=float(input("Enter first number: "))
           num2=float(input("Enter second number: "))
        except ValueError:
           print("invalid input","please use a number")
           continue

        if A == "1":
           print(num1,"+",num2,"=",add(num1,num2))
        elif A == "2":
           print(num1, "-", num2, "=",subtract(num1, num2))

        elif A == "3":
           print(num1,"/",num2,"=",divide(num1,num2))

        elif A == "4":
           print(num1,"×",num2,"=",multiply(num1,num2))
