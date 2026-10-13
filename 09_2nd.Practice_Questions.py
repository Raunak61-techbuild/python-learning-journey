#PRINT IF MULTIPLE OF 5
# n = int(input("Enter a number : "))
# if (n%5 == 0):
#     print("Multiple of 5")
# else:
#     print("Not a multiple of 5")
from symbol import return_stmt

#Print if ODD or EVEN
# n = int(input("Enter a number: "))
# if (n%2 == 0):
#     print("The number is even")
# else:
#     print("The number is odd")


#print multiplication table for any number n [using while]
# n = int(input("Enter a Number : "))
# i = 1

# while i<=10:
#     print(i*n)
#     i+=1


#print ODD Numbers from 1-10
# i = 0
# while i < 10:
#     i+=1
#     if i%2 == 0:
#         continue
#     print(i)


#Count vowels in a word
# word = "artificial intelligence"
# count = 0
#
# for ch in word:
#    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" :
#        count += 1
#
# print("Count of vovels =", count)


#Sum of First n Natural number
# number = int(input("Enter a number: "))
# Sum = 0
#
# for i in range(1 , number + 1):
#     Sum+=i
# print("The Sum is", Sum)


#TO PRINT FACTORIAL
# def print_factorial(n):
#     if n == 0:
#         return 1
#     return n * print_factorial(n-1)
# print(print_factorial(13))

#To return the largest out of three
# def return_largest(a,b,c):
#     if a > b:
#         return a
#     elif b < c:
#         return c
#     else:
#         return b
# print(return_largest(1,2,3))


#Q1. Takes salary as input. (To use conditional Statements)
# Salary = int(input("Enter a number : "))
#
# if (Salary < 30000):
#     print("Final Tax Rate is 5%")
# elif (Salary >= 30000 and Salary <= 70000):
#     print("Final Tax Rate is 15%")
# else:
#     print("Final Tax Rate is 25%")

#Q2
# def print_even(a , b):
#     for i in range(a , b+1):
#         if (i%2 == 1):
#             continue
#         print(i)
# print_even(1, 11)


#Q3
# def print_digits(n):
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n // 10
# print_digits(222)



#Q4

#METHOD 1 (if/else)
# def count_digits(n):
#         if n < 10:
#             return 1
#
#         elif n < 100:
#             return 2
#
#         elif n < 1000:
#             return 3
#
#         else:
#             return 4
#
# print(count_digits(3450))


#METHOD 2
# def count_digits(n):
#     count = 0
#
#     while n > 0:
#         n = n // 10
#         count +=1
#
#     return count
#
# print(count_digits(3450))



#Q5
# def digit_sum(n):
#     total = 0
#
#     while n > 0:
#         total = total + (n % 10)
#         n = n // 10
#     return total
#
# print(digit_sum(345))



#Q6
# for i in range (1, 101):
#     if (i%3 == 0 and i%5 == 0):
#         print(i)


#Q7
# def cont_input(n):
#     if n < 0:
#         return "Negative"
#     elif n > 0:
#         return "Positive"
#     else:
#         return "Zero"
#
# while True:
#     user_input = input("Enter a number or Quit : ")
#
#     if user_input == 'Quit':
#         break
#
#     n = int(user_input)
#     print(cont_input(n))


#Q8
# def calculator(a, b, operation):
#     if operation == '+':
#         return a+b
#     elif operation == '-':
#         return a-b
#     elif operation == '*':
#         return a*b
#     elif operation == '/':
#         return a/b
#     else:
#         return "error"
#
# print(calculator(4,2,'+'))



# Q9
# def is_prime(n):
#     if n < 2:
#         return False
#
#     for i in range(2, n):
#         if (n%i == 0):
#             return False
#     return True
#
# print(is_prime(4))


#Q10 (Number Guessing Game)
# def num_guess():
#     secret_num = 46
#
#     while True:
#         guess = int(input("Guess the number: "))
#
#         if guess > secret_num:
#             print("Too high")
#
#         elif guess < secret_num:
#             print("Too Low")
#
#         else:
#             print("Correct!")
#             break
#
# num_guess()





