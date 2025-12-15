"""
PYTHON ASSIGNMENT
Name: Durgesh Sharma
Course: 
Data Science With Generative AI Course
Institute: PW Skills
Topic: Basics of Python
"""

# --------------------------------------------------
# Q1. Explain the key features of Python that make it a popular choice for programming.

# Python is a high-level programming language known for its simple and readable syntax.
# It is easy to learn and beginner-friendly. Python supports object-oriented,
# procedural, and functional programming. It is open-source, platform independent,
# and has a large standard library. Python is widely used in web development,
# data science, artificial intelligence, and automation.

# --------------------------------------------------
# Q2. Describe the role of predefined keywords in Python and provide examples.

# Predefined keywords are reserved words in Python that have special meanings.
# They cannot be used as variable or function names. Keywords help define
# the structure and logic of a Python program.

# Example:
if True:
    print("Example of keyword: if")

for i in range(3):
    print(i)

def add(a, b):
    return a + b

# --------------------------------------------------
# Q3. Compare and contrast mutable and immutable objects in Python with examples.

# Mutable objects can be changed after creation, while immutable objects cannot.
# Mutable objects: list, dictionary, set
# Immutable objects: int, float, string, tuple

my_list = [1, 2, 3]
my_list[0] = 10

x = 5
x = 10

# --------------------------------------------------
# Q4. Discuss the different types of operators in Python with examples.

a = 10 + 5          # Arithmetic operator
print(a)

print(10 > 5)      # Relational operator
print(True and False)  # Logical operator

x = 5
x += 2             # Assignment operator
print(x)

print('a' in 'apple')  # Membership operator

# --------------------------------------------------
# Q5. Explain the concept of type casting in Python with examples.

num_str = "25"
num_int = int(num_str)
num_float = float(num_int)

print(num_int)
print(num_float)

# --------------------------------------------------
# Q6. How do conditional statements work in Python?

marks = 70

if marks >= 60:
    print("First Division")
elif marks >= 45:
    print("Second Division")
else:
    print("Fail")

# --------------------------------------------------
# Q7. Describe the different types of loops in Python.

# For loop
for i in range(5):
    print(i)

# While loop
i = 1
while i <= 5:
    print(i)
    i += 1

# --------------------------------------------------
print("ASSIGNMENT COMPLETED")