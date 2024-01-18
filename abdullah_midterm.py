# Abdullah Mid Term Exam
# Q1 - Write a Python program to do arithmetical operations addition and division.
num1=int(input("First Number"))
num2=int(input("Second Number"))
sum=num1+num2
division=num1/num2
print("Addition")
print("Sum of ",num1,"and",num2,"is",sum)
print("Division")
print("Division of ",num1,"and",num2,"is",division)

# Q2 - Write a Python program to find the area of a triangle

base=int(input("Base: "))
height=int(input("Height: "))
area=1/2*(base*height)
print("Area of Triangle is ",area)

# Q3- Write a Python program to convert Celsius to Fahrenheit.

celcius=float(input("Temperature in Celcius"))
farhenheit=(9/5*celcius+32)
print("Temperature in Farhenheit",farhenheit)

# Q4 - Write a Python program that return all datatypes that we discussed in the class.

name=input("Name: ")
print("This datatype is of ",type(name))

num=int(input("Number: "))
print("This datatype is of ",type(num))

fl=float(input("Float Number: "))
print("This datatype is of ",type(fl))

bo=bool(input("Boolean: "))
print("This datatype is of ",type(bo))