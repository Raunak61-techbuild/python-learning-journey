#1. Check whether it's palindrome or not (Using Loop)

# Name1 = "racecar"
# indx = -1
# reverse = ""
#
# for char in Name1:
#     reverse += Name1[indx]
#     indx -= 1
#
# if Name1 == reverse:
#     print("Same")
# else:
#     print("Different")



#2. Average of all Numbers in a list
# Integers = [-1, 2, 4, 8 , 0]
# total = 0
#
# for bit in Integers:
#     total += bit
#
# average = total/len(Integers)
# print(average)


#3. Input 2 lists of Integer from the USER

# list1 = [10, 8, 7, 4]
# list2 = [8, 9, 5 , 2]
#
# List3 = list1 + list2
# List3.sort()
# print(List3)


#4. From a tuple - print even, print odd

# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# even = () #I have to take () here.
# odd = ()

# for num in t:
#     if num % 2 == 0:
#         even += (num,) #we have to take this way to form a tuple
#     else:
#         odd += (num,) #we have to take this way to form a tuple

# print("Even numbers: ", even)
# print("Odd numbers:", odd)



#5. Dictionary to preserve marks

# student_marks = {
#     "Raunak" : 97 ,
#     "Adyan" : 85 ,
#     "Aditya" : 91
# }
#
# def menu_based (student_marks):
#     choice = input("Enter your choice (A/B/C/D): ").upper() #Converts input into Uppercase
#
#     if choice == 'A':
#         name = input("Enter student name: ")
#         marks = int(input("Enter marks: "))
#         student_marks[name] = marks
#         print("Student added successfully")
#
#     elif choice == 'B':
#         name = input("Enter student name: ")
#         marks = int(input("Enter updated marks: "))
#         student_marks[name] = marks
#         print("Marks updated successfully!")
#
#     elif choice == 'C':
#         name = input("Search for a student: ")
#         print(student_marks.get(name, "Student not found"))
#
#     elif choice == 'D':
#         print(student_marks)
#
#     else:
#         print("Invalid choice!")
#
# menu_based(student_marks)



#6. Creating a dictionary that maps each word to its length

# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# word_lengths = {}
#
# for word in words:
#     word_lengths[word] = len(word)
# print(word_lengths)



#7. Write a program that takes string from user and prints number of spaces

# S = input("Enter a String: ")
# s_num = 0
#
# for gap in S:
#     if gap == " ":
#         s_num += 1
# print(s_num)



#8. To check whether 2 lists share no common elements
# list1 = [1, 2, 3, 4]
# list2 = [4, 5, 6, 7]
#
# set1 = set(list1)
# set2 = set(list2)
#
# if set1.intersection(set2):
#     print("Common elements exist")
# else:
#     print("No Common elements")



#9. Print elements that appear more than once
# list = [3, 4, 5, 5, 6, 8, 2, 10]
#
# set1 = set()
#
# for num in list:
#     if list.count(num) > 1:
#         set1.add(num)
# print(set1)



#10. Ask for string and print unique characters and it's count
S = input("Enter a String: ")
unique = ""

for char in S:
    if char not in unique:
        unique += char

print("Unique characters:", unique)
print("Count of unique characters:", len(unique))
