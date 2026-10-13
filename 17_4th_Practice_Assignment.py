#Q1
#Bank_Account class , account_number, owner_name, balance
#Add methods to deposit , withdraw and check balance

# class BankAccount:
#     def __init__(self):
#         self.account_number = 47678
#         self.owner_name = "Rashmi"
#         self.balance = 67_000
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Money deposited: {amount}")
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Money withdrawn: {amount}")
#
#         else:
#             print("Insufficient balance!")
#
#     def check_balance(self):
#         print(f"Current balance: {self.balance}")
#
# # Create an object
# b1 = BankAccount()
#
# # Call the methods
# b1.deposit(5000)
# b1.withdraw(2000)
# b1.check_balance()




#Q2
#Class Book - title , author, list of reviews
#Add methods to - (i) add a new review , (ii) count reviews, (iii) display all reviews

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.list_of_reviews = []
#
#     def add_review(self, review):
#         self.list_of_reviews.append(review)
#         print("Review added succesfully!")
#
#     def count_reviews(self):
#         print(f"Total number of reviews: {len(self.list_of_reviews)}")
#
#     def display_reviews(self):
#         print(f"Reviews for {self.title}: ")
#         for review in self.list_of_reviews:
#             print(review)
#
#
# r1 = Book("The Alchemist", "Paulo Coelho")
#
# r1.add_review("An Inspiring Book.")
# r1.add_review("A wonderful story.")
#
# r1.count_reviews()
# r1.display_reviews()



#Q3
#class Student with private attrubutes => _name, _roll_no, _marks
#provide getter and setter methods with validation
#marks can't be negative , roll number has to be b/w 1-100 , name can't be empty

# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.__name = ""
#         self.__roll_no = 1
#         self.__marks = 0
#
#         self.set_name(name)
#         self.set_roll_no(roll_no)
#         self.set_marks(marks)
#
#     #Getters
#     def get_name(self):
#         return self.__name
#
#     def get_roll_no(self):
#         return self.__marks
#
#     def get_marks(self):
#         return self.__marks
#
#     #Setters with validation
#     def set_name(self, new_name):
#         if new_name.strip():
#             self.__name = new_name
#         else:
#             print("Name cannot be empty!")
#
#     def set_roll_no(self, new_roll_no):
#         if 1 <= new_roll_no <= 100:
#             self.__roll_no = new_roll_no
#         else:
#             print("Roll number must be between 1 and 100!")
#
#     def set_marks(self, new_marks):
#         if new_marks >= 0:
#             self.__marks = new_marks
#         else:
#             print("Marks cannot be negative!")
#
# #Create an object
# s1 = Student("Raunak", 25, 97)
#
# #Get Values
# print(s1.get_name())
# print(s1.get_roll_no())
# print(s1.get_marks())
#
# #Update values
# s1.set_name("Rashmi")
# s1.set_roll_no(30)
# s1.set_marks(95)
#
# print(s1.get_name())
# print(s1.get_roll_no())
# print(s1.get_marks())



#Q4
#Class Shape with a method() area
#Create subclasses Circle, Rectangle and Triangle that override the area() method

# class Shape:
#     def area(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, Radius, PI):
#         self.Radius = Radius
#         self.PI = PI
#
#     def area(self):
#         return self.PI * self.Radius ** 2
#
#
# class Rectangle(Shape):
#     def __init__(self, Length, Width):
#         self.Length = Length
#         self.Width = Width
#
#     def area(self):
#         return self.Length * self.Width
#
#
# class Triangle(Shape):
#     def __init__(self, Width, Height):
#         self.Width = Width
#         self.Height = Height
#
#     def area(self):
#         return 0.5 * self.Width * self.Height
#
#
# c = Circle(5, 3.14159)
# r = Rectangle(4, 6)
# t = Triangle(8, 5)
#
# print(c.area())
# print(r.area())
# print(t.area())




#Q5
#Base Case Vehicle with attributes like brand and model
#Two Subclasses Car and Bike that add extra attributes
#(1) seats(in Car) & (2) engine_cc(in Bike)

# class Vehicle:
#     brand = "Maruti"
#     Model = "TUV350"
#
# class Car(Vehicle):
#     def __init__(self, Seats):
#         self.Seats = Seats
#
# class Bike(Vehicle):
#     def __init__(self, engine_cc):
#         self.engine_cc = engine_cc
#
# car1 = Car(5)
# bike1 = Bike(750)
#
# print(
#     car1.brand,
#     car1.Model,
#     car1.Seats,
#     bike1.brand,
#     bike1.Model,
#     bike1.engine_cc
# )


#Q6
#Abstract class Employee with abstract method calculate_salary()
#Create subclasses Intern, FullTimeEmployee, ContractEmployee

# from abc import ABC , abstractmethod
#
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
# class Intern(Employee):
#     def calculate_salary(self):
#         print("He earns less than 10k!")
#
# class FullTimeEmployee(Employee):
#     def calculate_salary(self):
#         print("He earns around 100k!")
#
# class ContractEmployee(Employee):
#     def calculate_salary(self):
#         print("He earns around 50k!")
#
# intern = Intern()
# intern.calculate_salary()
#
# fT = FullTimeEmployee()
# fT.calculate_salary()
#
# cT = ContractEmployee()
# cT.calculate_salary()



#Q7
#Class Person that allows constructor to work with:
# name only , name + age , name + age + address
# Direct constructor overloading(multiple constructors) are not allowed but we have to use default
# parameters to simulate constructor overloading

# class Person:
#     def __init__(self, name, age=None, address=None):
#         self.name = name
#         self.age = age
#         self.address = address
#
#
# p1 = Person("Raunak")
# p2 = Person("Rashmi", 18)
# p3 = Person("Anshu", 18, "India")
#
# print(p1.name, p1.age, p1.address)
# print(p2.name, p2.age, p2.address)
# print(p3.name, p3.age, p3.address)



#Q8
#Class Player
# a Class Variable player_count
# instance variables name and level

# class Player:
#     player_count = 0
#
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#         Player.player_count += 1
#
# p1 = Player("Raunak", 5)
# p2 = Player("Aditya", 8)
# p3 = Player("Adyan", 6)
#
# print(p1.name, p1.level)
# print("Total players:", Player.player_count)



#Q9
# Creating the following classes : Herbivore , Carnivore , Omnivore with attributres & methods
# Create class Bear that inherits from all classes to showcase multiple inheritance


class Herbivore:
    def __init__(self, grass):
        self.grass = grass


class Carnivore:
    def __init__(self, meat):
        self.meat = meat


class Omnivore:
    def __init__(self, egg):
        self.egg = egg


class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, grass, meat, egg):
        Herbivore.__init__(self, grass)
        Carnivore.__init__(self, meat)
        Omnivore.__init__(self, egg)


eat = Bear("Green", "Chicken", "Poultry")
print(eat.grass, eat.meat, eat.egg)
