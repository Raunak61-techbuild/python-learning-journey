#Q1
#Opens a file names.txt in write mode
#Write 5 names (one per line) entered by the user
#Opens same line in read mode and prints all names

# f = open("names.txt", "w")
#
# for i in range(5):
#     name = input(f"Enter name {i + 1}: ")
#     f.write(name + "\n")
#
# f.close()
#
# f = open("names.txt", "r")
# content = f.read()
# f.close()
#
# print(content)



#Q2
#Opens file "log.txt" in append mode
#Adds new log entry(like "Program run successfully")
#Opens file in read mode and print all logs

# f = open("log.txt", "a")
# f.write("Program run succesfully\n")
# f.close()
#
# f = open("log.txt", "r")
# content = f.read()
# f.close()
# print(content)



#Q3
#Program must have list of num:[5, 10, 15, 20, 25]
#Uses list comprehension to create new list with num < 15
#print new list

# numbers = [5, 10, 15, 20, 25]
# new_list = [num for num in numbers if num > 15]
# print(new_list)



#Q4
#Ask user for a new city & its population
#Update this info in the json file
#Ask user for a new city & its population - update this info in json file


import json

# 1. Create a dictionary of 3 cities and their populations
# data = {
#     "Delhi": "23 Million People",
#     "Jharkhand": "33 Million People",
#     "Karnataka": "74 Million People"
# }
#
# # 2. Save the dictionary to cities.json
# with open("cities.json", "w") as f:
#     json.dump(data, f, indent=3, sort_keys=True)
#
# # 3. Load the JSON file and print each city and its population
# with open("cities.json", "r") as f:
#     data = json.load(f)
#
# for city, population in data.items():
#     print(f"{city}: {population}")
#
# # 4. Ask the user for a new city and its population
# new_city = input("\nEnter a new city: ")
# new_population = input("Enter its population: ")
#
# # 5. Update the dictionary
# data[new_city] = new_population
#
# # 6. Save the updated dictionary to the JSON file
# with open("cities.json", "w") as f:
#     json.dump(data, f, indent=3, sort_keys=True)
#
# print("\nUpdated cities.json successfully!")




#Q5
# Write a program that tries to open data.txt"
# in read mode. If the file does not exist, catch the exception and print "File not found!".

try:
    f = open("data.txt", "r")
    content = f.read()
    print(content)

except FileNotFoundError:
    print("File not found!")







