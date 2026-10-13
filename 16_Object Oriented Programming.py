# ============================================================
# OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================================

# Class - Blueprint or template for creating objects.

# ============================================================
# 1. CLASSES AND OBJECTS
# ============================================================

# class Car:
#     brand = "Suzuki"
#
# car1 = Car()
# car2 = Car()
#
# print(car1.brand)
# print(car2.brand)


# ============================================================
# 2. CONSTRUCTORS
# ============================================================

# ------------------------------------------------------------
# Default Constructor
# ------------------------------------------------------------

# class Student:
#     def __init__(self):
#         print("Constuctor was called")
#
# stu1 = Student()
# stu2 = Student()

# ------------------------------------------------------------
# Parameterized Constructor
# ------------------------------------------------------------

# Using a constructor to initialize values.

# class Student:
#     def __init__(self, name):
#         self.name = name
#
# stu1 = Student("Raunak")
# stu2 = Student("Rashmi")
#
# print(stu1.name, stu2.name)


# ============================================================
# 3. ATTRIBUTES
# ============================================================

# Attributes are variables that belong to a class or object.


# ------------------------------------------------------------
# Class Attributes
# ------------------------------------------------------------

# class Student:
#     college = "GD Goenka University"
#
# stu1 = Student()
#
# print(stu1.college)
# print(Student.college)
# Class attributes can also be accessed using the class name.


# ------------------------------------------------------------
# Instance Attributes
# ------------------------------------------------------------

# class Student:
#     def __init__(self, name, sgpa):
#         self.name = name
#         self.sgpa = sgpa
#
# stu1 = Student("Raunak", 9.7)
#
# print(stu1.name, stu1.sgpa)


# ============================================================
# 4. METHODS IN OOP
# ============================================================

# There are three types:
# 1. Instance Method
# 2. Class Method
# 3. Static Method

# class Laptop:
#     storage_type = "SSD"
#
#     def __init__(self, RAM):
#         self.RAM = RAM
#
#     def get_info(self):                  # Instance Method
#         print(
#             f"Laptop has {self.RAM} RAM "
#             f"& storage type is {self.storage_type}"
#         )
#
#     @staticmethod
#     def get_storage_type(cls):           # Class Method
#         print(f"Storage type is {cls.storage_type}")
#
#     @classmethod
#     def cal_discount(price, discount):   # Static Method
#         final_price = price - (price * discount / 100)
#         print(f"Final price = {final_price}")
#
# l1 = Laptop("16 GB")
#
# l1.get_info()
# Laptop.get_storage_type()
# l1.cal_discount(40_000, 10)


# ============================================================
# 5. PRACTICE PROBLEM: ONLINE STORE
# ============================================================

# Requirements:
# 1. Create products with a name and price.
# 2. Track the total number of products created.
# 3. Create a static method to calculate a discount.

# class Product:
#     count = 0
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.count += 1
#
#     def get_info(self):
#         print(f"Price of {self.name} is {self.price}")
#
#     @classmethod
#     def get_count(cls):
#         print(f"Total products in store = {cls.count}")
#
#     @staticmethod
#     def calc_discount(price, discount):
#         discounted_price = price - (price * discount / 100)
#         print(f"Discounted price = {discounted_price}")
#
#
# p1 = Product("iPhone 16 Plus", 99_000)
# p2 = Product("MacBook Air M4", 119_000)
# p3 = Product("AirPods Pro", 24_500)
#
# p1.get_info()
# p2.get_info()
# p3.get_info()
#
# Product.get_count()
# Product.calc_discount(10_000, 1)


# ============================================================
# 6. ENCAPSULATION
# ============================================================

# Encapsulation combines data and methods inside a class.
# __balance demonstrates name-mangled attribute access.

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name             # Public attribute
#         self.__balance = balance     # Name-mangled attribute
#
#     def get_balance(self):           # Getter
#         return self.__balance
#
#     def set_balance(self, new_balance):  # Setter
#         self.__balance = new_balance
#
# acc1 = BankAccount("Rahul", 50_000)
#
# print(acc1.get_balance())
#
# acc1.set_balance(60_000)
# print(acc1.get_balance())


# ============================================================
# 7. INHERITANCE
# ============================================================

# ------------------------------------------------------------
# Single Inheritance
# ------------------------------------------------------------

# class Employee:
#     start_time = "9 AM"
#     end_time = "5 PM"
#
# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject = subject
#
# t1 = Teacher("Data Science")
#
# print(t1.subject, t1.start_time, t1.end_time)


# ------------------------------------------------------------
# Multilevel Inheritance
# ------------------------------------------------------------

# class Employee:
#     start_time = "9 AM"
#     end_time = "5 PM"
#
# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role
#
# class Accountant(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init__(role)
#         # super() calls the parent class constructor.
#         self.salary = salary
#
# acc1 = Accountant(50_000, "CA")
#
# print(
#     acc1.salary,
#     acc1.role,
#     acc1.start_time,
#     acc1.end_time
# )


# ------------------------------------------------------------
# Multiple Inheritance
# ------------------------------------------------------------

# class Teacher:
#     def __init__(self, salary):
#         self.salary = salary
#
# class Student:
#     def __init__(self, gpa):
#         self.gpa = gpa
#
# class TA(Teacher, Student):
#     def __init__(self, name, salary, gpa):
#         super().__init__(salary)
#         Student.__init__(self, gpa)
#         self.name = name
#
# ta = TA("Rahul", 50_000, 7.5)
#
# print(ta.name, ta.salary, ta.gpa)


# ============================================================
# 8. ABSTRACTION
# ============================================================

# Abstraction hides implementation details and defines
# methods that subclasses must implement.

# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")
#
# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!")
#
# lion = Lion()
# lion.make_sound()
#
# cow = Cow()
# cow.make_sound()


# ============================================================
# 9. POLYMORPHISM
# ============================================================

# ------------------------------------------------------------
# Function Overriding (Method Overriding)
# ------------------------------------------------------------

# class Animal:
#     def sound(self):
#         print("Some generic sound")
#
#
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
#
#
# a = Animal()
# dog = Dog()
#
# a.sound()
# dog.sound()


# ------------------------------------------------------------
# Duck Typing
# ------------------------------------------------------------

# class Dog:
#     def speak(self):
#         print("Bark")
#
#
# class Cat:
#     def speak(self):
#         print("Meow")
#
#
# class Robot:
#     def speak(self):
#         print("Beep Boop")
#
#
# def make_it_speak(entity):
#     entity.speak()
#
#
# d = Dog()
# c = Cat()
# r = Robot()
#
# for e in [d, c, r]:
#     make_it_speak(e)


