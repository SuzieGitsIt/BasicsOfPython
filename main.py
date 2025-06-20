suzie_path = r"C:\Users\Susan\OneDrive\Documents\Python\BasicsOfPython/"

# 1. Mutable vs immutable types
# Mutable example (list) allow modification once created (append)
my_list = [1, 2, 3]
my_list.append(4)  # Modifies the original list
print("Mutable Example (list): ", my_list)          # [1, 2, 3, 4]

# Immutable example (string) do not allow modification once created
my_string = "hello"
new_string = my_string + " world"  # Creates a new string
print("I always get A++", my_string)                # hello
print("Immutable Example (string): ", new_string)   # hello world

# Tuples, lists, dictionaries, sets
# Tuples are immutable
my_tuple = (1, "hello", 3.14)
print("Tuple example (immutable): ", my_tuple)   # (1, "hello", 3.14)

# Lists are mutable
# Lists are ordered, mutable, and allow duplicates
my_list = [1, "hello", 3.14]
print("List example (mutable): ", my_list)       # [1, "hello", 3.14]

my_list.append(True)
print("List example (mutable): ", my_list)       # [1, "hello", 3.14, True]

# Dictionaries are mutable
my_dict = {"name": "Susan", "age": 30, "city": "New York"}
print("Dictionary example (mutable): ", my_dict)         # {'name': 'Suzie', 'age': 30, 'city': 'New York'}
print("Dictionary example (mutable): ", my_dict["age"])  # 30

# Sets are mutable (add)
# Sets do not allow duplicates
my_set = {1, 2, 2, 3, 3, 3}
print("Sets example (mutable): ", my_set)        # {1, 2, 3}
my_set.add(4)
print("Sets example (mutable): ", my_set)        # {1, 2, 3, 4}

# List/dict/set comprehensions
# List comprehension
x = [i for i in range(10)]  
print("List comprehension: ", x)                 # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [i for i in range(10) if i > 5]             
print("List comprehension: ", x)                 # [6, 7, 8, 9]
list_comp = [(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y]
print("List comprehension: ", list_comp)         # [(1, 3), (1, 4), (2, 3), (2, 1), (3, 4)]

# Dictionary comprehension
dict1 = dict([(i, i+10) for i in range(4)])
print("Dictionary comprehension: ", dict1)       # {0: 10, 1: 11, 2: 12, 3: 13}
dict2 = {i : i+10 for i in range(4)}
print("Dictionary comprehension: ", dict2)       # {0: 10, 1: 11, 2: 12, 3: 13}
dict3 = {(k, v): k+v for k in range(2) for v in range(2)}
print("Dictionary comprehension: ", dict3)       # {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 2}

# Set comprehension, Creating a set of squares
numbers = [1, 2, 3, 4, 5]
squares_set = {x**2 for x in numbers}           # Creates a set of squares
print("Set comprehension: ", squares_set)        # {1, 4, 9, 16, 25}

# Set comprehension, Creating a set of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_set = {x for x in numbers if x % 2 == 0}   # Creates a set of even numbers
print("Set comprehension: ", even_set)           # {2, 4, 6, 8, 10}

# Set comprehension, Creatig a set from a string, removing duplicates
sentence = "The cat in the hat had two sidekicks, thing one and thing two."
word_set = {word.lower() for word in sentence.split()}  # Converts words to lowercase and creates a set
print("Set comprehension, word set: ", word_set)  # {'the', 'one', 'thing', 'and', 'in', 'two', 'sidekicks,', 'had', 'cat', 'hat'}

# Set comprehension, Creating a set from multiple lists, handling duplicates
list1 = [1, 2, 3, 3]
list2 = [3, 4, 5, 5]
combined_set = {x for x in list1 for y in list2 if x == y}  # Creates a set of numbers present in both lists
print("Set comprehension: ", combined_set)       # {3}

# 2. Functions
# Default, keyword, and variable-length arguments (*args, **kwargs)
# Default argument allow you to set a default value for a parameter
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet("Suzie")
greet("Bob", "Good morning")

def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")
describe_person(name='Suzie', age=30, city="New York")
describe_person(age=25,city="Los Angeles", name="Bob")

# Variable-length arguments allow you to pass a variable number of arguments to a function
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print("*args Add numbers: ", add_numbers(1,2,3))     # 6
print("*args Add numbers: ", add_numbers(4,5,6,7,8)) # 30

# Keyword arguments allow you to pass arguments by name
def print_info(**kwargs):
    for key, value in kwargs.items():
        print("**kwargs Keyword Arguments: ", f"{key}: {value}")

print_info(name="Eve", age=28, occupation="Engineer")
# Output:
# name: Eve
# age: 28
# occupation: Engineer

# Lambda functions
# Lambda function, adding two numbers
add = lambda x, y: x + y
result = add(5, 3)
print("Lambda function, add: ", result)          # 8

# Lambda function, checking if a number is even
is_even = lambda x: x % 2 == 0
result = is_even(4)
print("Lambda function, is even: ", result)      # True

# Lamda function, converting celsius to fahrenheit
c_to_f = lambda c: (c * 9/5) + 32
result = c_to_f(0)
print("Lambda function, C to F: ", result)       # 32.0

# Closures and scopes
# Closure is a function object that remembers values in enclosing scopes even if they are not present in memory
def multiplier(x):
    def inner(y):
        return x * y
    return inner

multiply_by_5 = multiplier(5)
print("Closures: ", multiply_by_5(10))           # 50

multiply_by_3 = multiplier(3)
print("Closures: ", multiply_by_3(10))           # 30

# Scopes
global_var = 10

def outer_function():
    outer_var = 20
    def inner_function():
        inner_var = 30
        print("Scopes: ", inner_var, outer_var, global_var) # Accessing local, enclosing, and global variables
    inner_function()

outer_function()  # 30 20 10

# 3. Control Flow
# Loops (for, while)
# For Loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("For Loop:", fruit)        # apple, banana, cherry

for char in "Hello":
  print("For Loop:", char)           # H, e, l, l, o

for i in range(5):      
  print("For Loop:", i)             # Iterates from 0 to 4

colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print("For Loop ", f"Index: {i}, Color: {colors[i]}")  # Index: 0, Color: red, Index: 1, Color: green, Index: 2, Color: blue

# While Loops
count = 0
while count < 5:
  print("While Loop ", f"Count is: {count}")   # Count is: 0, Count is: 1, Count is: 2, Count is: 3, Count is: 4
  count += 1

number = 10
while number > 0:
    print("While Loop: ", number)           # 10, 8, 6, 4, 2
    number -= 2

i = 1
while i < 10:
    print("While Loop: ", i)
    if i == 5:
        break
    i += 1

counter = 0
while counter < 3:
    print("Inside loop")
    counter += 1
else:
    print("Inside else block")

# Conditionals
# Simple if statement
x = 10
if x > 5:
    print("Conditional: x is greater than 5")

# if-else statement
y = 3
if y > 5:
    print("Conditional: y is greater than 5")
else:
    print("Conditional: y is not greater than 5")

# if-elif-else statement
z = 7
if z > 10:
    print("Conditional: z is greater than 10")
elif z > 5:
    print("Conditional: z is greater than 5 but not greater than 10")
else:
    print("Conditional: z is not greater than 5")

# Nested if statements
a = 12
if a > 5:
    print("Conditional: a is greater than 5")
    if a < 15:
        print("Conditional: a is also less than 15")

# Conditional expressions (ternary operator)
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Conditional: ", status)   # Adult

# Checking multiple conditions with logical operators
temperature = 25
if temperature > 20 and temperature < 30:
    print("Conditional: The temperature is comfortable")
    
# Using "in" operator for string or list
name = "Susan"
if "A" in name:
    print("Conditional: Name contains 'A'")

# Checking for empty list
my_list = []
if not my_list:
    print("Conditional: The list is empty")

# Ternary operator AKA conditional operator/expression.
# A shortcut for writing simple if-else statements
# It evaluates a condition and returns one of two values based
# on whether the condition is true or false
age = 17
status = "Adult" if age >= 18 else "Minor"
print("Ternary operator: ", status)            # Minor

x = 10
y = 5
max_value = x if x > y else y
print("Ternary operator: ", max_value)         # 10

is_raining = True
activity = "Stay inside" if is_raining else "Go outside"
print("Ternary operator: ", activity)          # Stay inside

number = 7
parity = "Even" if number % 2 == 0 else "Odd"
print("Ternary operator: ", parity)            # Odd

# Generator expressions
# Simple Generator Function
def number_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1
for num in number_generator(5):             # Using the generator
    print("Generator Function: ", num)       # 0, 1, 2, 3, 4

# Generator Expression
squares = (x**2 for x in range(5))
for square in squares:                      # Using the generator
    print("Generator Expression: ", square)  # 0, 1, 4, 9, 16

# Generator for File Reading
def file_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
for line in file_reader(suzie_path+"example.txt"):     # Using the generator
    print("Generator Expression: ", line)

# Generator Yield From
def sub_generator(n):
    for i in range(n):
        yield i

def main_generator(n):
    yield from sub_generator(n)
    yield from range(n, n + 3)
for num in main_generator(3):            # Using the generator
    print("Generator Yield From: ", num)

# 4. Object-Oriented Programming (OOP)
# Classes and instances
# Class Dog, Instance/object my_dog
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", "Golden Retriever")
print("Class: Dog: ", my_dog.name)       # Buddy
print("Instance: ", my_dog.bark())       # Woof!

# __init__, __str__, __repr__
# __init__ method is a constructor, called when an object is created
# __str__ AKA Dunder (double underscore) method is used to define a string representation of the object
# __repr__ method is used to define a more formal string representation of the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

person1 = Person("Suzie", 30)
print("__str__", str(person1))   # Person(name='Suzie', age=30)
print("__str__", person1)        # Person(name='Suzie', age=30)

# __repr__ method is used to define a more formal string representation of the object
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"MyClass({self.x}, {self.y})"

obj = MyClass(2, 3)
print("__repr__", repr(obj))        # Expected output: MyClass(2, 3)

# Inheritance and method overriding
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

my_dog = Dog("Buddy", "Golden Retriever")
print("Inheritance and method overriding ", my_dog.name)   # Buddy
print("Inheritance and method overriding ", my_dog.breed)  # Golden Retriever
print("Inheritance and method overriding ", my_dog.speak())  # Woof!

# 5. Error Handling
# try, except, finally, else
# Example 1: try and except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Try and except ", f"Error: {e}")

# Example 2: try, except, and else
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Try, except and else: Invalid input. Please enter a valid integer.")
# else:
#     print("Try, except and else ", f"You entered: {num}")

# Example 3: try, except, and finally
try:
    f = open(suzie_path+"my_file.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("Try, except, else and finally: File not found.")
finally:
    try:
        f.close()
    except NameError:
        pass
    print("Try, except, else and finally: Closing the file.")

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Try, except, else and finally: Cannot divide by zero!")
    else:
        print("Try, except, else and finally: The result is", result)
    finally:
        print("Try, except, else and finally: Execution completed")

divide(10, 2)
divide(10, 0)

# Custom exceptions
# CustomError, SpecificErrorA SpecificErrorB
class CustomError(Exception):   # Base class for other exceptions
    pass

class SpecificErrorA(CustomError): # Raised when a specific problem A happens
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class SpecificErrorB(CustomError):  # Raised when a specific problem B happens
    def __init__(self, message, detail):
      self.message = message
      self.detail = detail
      super().__init__(self.message)

# Example usage
def process_data(value):
    if value < 0:
        raise SpecificErrorA("Custom Exception: Value cannot be negative")
    if value > 100:
        raise SpecificErrorB(" Custom Exception: Value is too large", "Maximum allowed value is 100")
    return "Data processed successfully"

try:
    result = process_data(-5)
    print(result)
except SpecificErrorA as e:
    print(f"Custom Exception: Error: {e.message}")
except SpecificErrorB as e:
    print(f"Custom Exception: Error: {e.message}, Details: {e.detail}")
except Exception as e:
    print(f"Custom Exception: An unexpected error occurred: {e}")

# 6. Modules and Imports
# Standard libraries like math, random, datetime, os, sys
import math
print(math.sqrt(25))                # 5.0
print(math.pi)                      # 3.141592653589793
print(math.sin(math.radians(30)))   # 0.49999999999999994

import random
print(random.random())              # Random float between 0.0 and 1.0
print(random.randint(1,10))         # Random integer between 1 and 10
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)             # Shuffle the list in place
print("Random shuffle: ", my_list)  # Randomly shuffled list

import datetime
now = datetime.datetime.now()
print("Current date and time: ", now)  # Current date and time
print("Current date: ", now.year, now.month, now.day)  # Current date
print(now.strftime("%Y-%m-%d %H:%M:%S")) # Formatted date and time

import os
print("Current working directory: ", os.getcwd())  # Current working directory
# print(os.listdir())                             # Lists all directories in User/Susan 

import sys
print("Python version: ", sys.version)  # Python version
print("OS platform: ", sys.platform)    # OS platform
# sys.exit()                           # Exit the program

# Import patterns: import x, from x import y
from os import path, getcwd
current_directory = getcwd()            # no 'os.' prefix needed
print(f"The current directory is: {current_directory}")

import numpy as np
array = np.array([1, 2, 3])
print("Numpy array: ", array)           # [1 2 3]

# 7. File I/O
# Reading and writing text files
# Writing to a file
# Context managers (with open(...))
f = suzie_path+"new_file.txt"
with open(f, "w+") as file:
    file.write("Hello good sir and madam.\n")
    file.write("This is a new line.\n")
    file.write("This is another line.\n")
    print("File I/O: File written successfully.")
    file.close()

# Appending to a file
with open(f, "a+") as file:
    file.write("This is an appended line.\n")
    print("File I/O: File appended successfully.")
    file.seek(0)
    file.flush()

# Reading the entire file
with open(f, "r+") as file:
    stuff = file.read()
    print("File I/O: File content:")
    print({stuff})
    file.close()

# Reading line by line
with open(f, "r+") as file:
    for line in file:
        print("File I/O: Line: ", line.strip())
        file.close

# Reading all lines into a list
with open(f, "r+") as file:
    lines = file.readlines()
    print("File I/O: All lines in a list ")
    for line in lines:
        print(line.strip())
    file.close()

# 8. Comprehensions & Iterators
# Nested list comprehensions
# Flatten the matrix into a single list
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print("Original list: ", matrix)             # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Nested list comprehensions: ", flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of squares for each number in the matrix
squares =[[num**2 for num in row] for row in matrix]
print("Nested list, list of squares:", squares)  # [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

# Filter even numbers and create a new matrix
even_matrix =[[num for num in row if num % 2==0] for row in matrix]
print("Nested list, filter even numbers:", even_matrix)  # [[2], [4, 6], [8]]

# similar, not nested code. Does not keep the structure of the matrix
event_matrix2 = []
for row in matrix:
    for num in row:
        if num % 2 == 0:
            event_matrix2.append(num)
print("Nested list comprehensions: ", event_matrix2)  # [2,4,6,8]

# Generators
# Simple counter generator
def count_up_to(n):
    count =1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(7)                    # Using the generator
for num in counter:
    print("Counter Generator: ", num)       # 1, 2, 3, 4, 5

# Fibonacci sequence generator
def fib_seq():
    a, b=0, 1
    while True:
        yield a
        a, b = b, a+b

fibonacci = fib_seq()                               # Using the generator
for _ in range(10):
    print("Fibonacci Generator: ", next(fibonacci))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Reading large files
# This generator reads a file line by line, which is memory efficient for large files
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
print("Reading large file line by line:")
for line in read_large_file(suzie_path+"large_file.txt"):      # Using the generator
    print(line)

# Generator expression
# A generator expression is a compact way to create a generator
# It uses a similar syntax to list comprehensions but uses parentheses instead of square brackets
# A consise way to create a genertor, similar to list comprehension
squares_gen=(x**2 for x in range(10))
for square in squares_gen:                  # Using the generator
    print("Generator expression: ", square) # 0, 1, 4, 9, 16, 25, 36, 49, 64, 81

# infinite sequence generator
def infinite_odd_nums():
    num = 1
    while True:
        yield num
        num += 2
odd_gen = infinite_odd_nums()                # Using the generator
for _ in range(5):
    print("Infinite odd numbers: ", next(odd_gen)) # 1, 3, 5, 7, 9

# 9. Decorators
# Basic decorator structure
def my_decorator(func):                     # Decorator function
    def wrapper(*args, **kwargs):           # Wrapper function
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator                               # syntacts sugar for say_hello = my_decorator(say_hello)
def say_hello(name):                        # Function to be decorated
    print(f"Hello, {name}!")                # Hello, Suzie!

say_hello("Suzie")

# Using functools.wraps
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        '''Wrapper function docstring'''
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper
@my_decorator
def my_function():
    '''My function docstring'''
    return x + y
print(my_function.__name__)
print(my_function.__doc__)

# 10. Miscellaneous
# is vs ==
# the 'is' operator checks if two variables refer to the same object
# in memory. It returns True or False.
# the '==' operator checks if two variables have the same value.
# It returns True or False.
a = [1, 2, 3]       # same value as b and c, == is True
b = [1, 2, 3]       # 
c = a               # a & c refer to the same object in memory 'is' True
                    # b = a or c to make 'is' True.
print("a is b: ", a is b)               # False
print("a is c: ", a is c)               # True
print("a == b: ", a == b)               # True
print("a == c: ", a == c)               # True

# b = a or c to make 'is' True.
b = c                       # since c is  equal to a, now b is too.
print("a is b: ", a is b) # Truealready

# None, truthy/falsy values
x = None
if not x:
    print("x is falsy (None)")

y = []
if not y:
    print("y is falsy (empty list)")

z = 10
if z:
    print("z is truthy (non-zero number)")

# Slicing and indexing
# [start:stop:step]
my_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(my_list[2:7])     # 20,30,40,50,60 --> start at 2, stop at 7 (exclusive)
print(my_list[:5])      # 0,10,20,30,40 --> start at 0, stop at 5 (exclusive)
print(my_list[5:])      # 50,60,70,80,90,100 --> start at 5, stop at end 
print(my_list[1:8:2])   # Step: i1, i1+step, i2+step, i3+step --> 10,30,50,70
print(my_list[::3])     # i1, i1+step, i2+step, i3+step --> 0,30,60,90
print(my_list[::-1])    # Reverse the list --> 100,90,80,70,60,50,40,30,20,10,0
print(my_list[::-2])    # Reverse the list with step --> 100,80,60,40,20
print(my_list[-5:-1])   # -5 to -1 --> 50,60,70,80,90
print(my_list[-1])      # Last element --> 100

step_list = []
for i in range(500):
    step_list.append(i)
#print("Step List Full: ", step_list)
print("Step List [0:50:3]: ", step_list[0:50:3])

# * unpacking and assignment
a, *b, c = [1, 2, 3, 4, 5]
print(a)   # 1
print(b)   # [2, 3, 4]
print(c)   # 5

x, *y = (10, 20, 30)
print(x)  # 10
print(y)  # [20, 30]

*z, w = "hello"
print(z)  # ['h', 'e', 'l', 'l']
print(w)  # o

*z, w = "hellomoto"
print(z)  # ['h', 'e', 'l', 'l', 'o', 'm', 'o']
print(w)  # o

x = "Hello"[0]
print(x)  # H

# x = "Hello".sub(0,1)   
# print(x)  # e for error

# x= sub("Hello", 0, 1)
# print(x)  # e for error

_myvar = 10
print(_myvar)  # 10

MyVar =5
print(MyVar)  # 5

#my-var = 22     # dashes are not allowed
#print(my-var)  # SyntaxError: invalid syntax

mystr ="hello"
mystr.upper()
print(mystr)  # hello

mystr = mystr.replace("h", "H")
print(mystr)  # Hello

a = int(5)
b = 5
print(a+b)  # 10

c = float(2.8)
d= 2.8
print(c+d)  # 5.6