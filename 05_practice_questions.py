#Q1
age = 18
print("Hello shraddha, you are", age, "years old")

#Q2
a = 5
b = 10

print(a+b)
print(a-b)
print(a*b)
print(a/b)



a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = float(input("Enter a number: "))
print(a+b+c)
average = (a+b+c)/3
print("The Average of the three numbers is ", average) 


#Q4
a = input("Enter a number: ")
print(int(a), type(int(a)))
print(float(a), type(float(a)))
print(str(a), type(str(a)))


#Q6
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

#We use this temporary variable to store the value of a, so that we can assign the value of b to a and then assign the value of temp to b.
temp = a
a = b
b = temp

print("The value of a is ", a) 
print("The value of b is ", b)


#Q7
Celsius_temp = float(input("Enter a temperature in Celsius: "))
Fahrenheit_temp = (Celsius_temp * (9/5)) + 32
print("The temperature in Fahrenheit is ", Fahrenheit_temp)



#Q8
Radius = float(input("Enter the radius of the circle : "))
PI = 3.14
print("Area of circle is : ", PI * Radius ** 2)

#Q9
P = float(input("Enter the Principal : "))
R = float(input("Enter the Rate : "))
T = float(input("Enter the Time : "))

SI = (P*R*T)/100
print(SI)


#Q10
a = float(input("Enter a number : "))
print("Integer Part : " , int(a))
print("Decimal Part : ", a - int(a))
