#Building Calculator 
a = int(input("Enter Your First Number - "))
b = int(input("Enter Your Second Number - "))

x = input("What Do you want to Perform  +,-,*,/,**,%,//  :-")

if x == "+":
    print(a+b)
if x == "-":
    print(a-b)
if x == "*":
    print(a*b)
if x == "/":
    print(a/b)
if x == "**":
    print(a**b)
if x == "%":
    print(a%b)
if x == "//":
    print(a//b)
