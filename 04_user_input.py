#Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name, age)

#input always begins with string
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(a+b) #(because both are integers they will be added)
#here similarly we can take float or any other data type input from user and perform operations on them


#print the average of 2 numbers
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
print(a+b)

a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
average = (a+b)/2
print("The Average of the two numbers is ", average) #(if i use + and i have to add str here)
