# Python Loops and Functions: Explanations and Examples

This document summarizes the concepts, explanations, and code examples from the notebook `el_python_d4.ipynb`. It covers loops (`for`, `while`), control statements, and user-defined functions in Python.

---

## Loops in Python

Loops are used to execute a block of code multiple times, either for a fixed number of iterations or infinitely (until a condition is met).

### For Loop

A `for` loop is typically used when you want to iterate a specific number of times or over a collection.

**Example: Print "Hello World" 5 times (without a loop):**
```python
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
```

**Example: Print "Hello World" 5 times using a for loop:**
```python
for i in range(0,5):
    print(i, "Hello World")
```
_Output:_
```
0 Hello World
1 Hello World
2 Hello World
3 Hello World
4 Hello World
```

**Example: Print "Hello World" for numbers 1 to 4:**
```python
for i in range(1,5):
    print(i, "Hello World")
```
_Output:_
```
1 Hello World
2 Hello World
3 Hello World
4 Hello World
```

**Example: Multiplication Table of 5 (without a loop):**
```python
print("5 * 1 = ", 5 * 1)
print("5 * 2 = ", 5 * 2)
print("5 * 3 = ", 5 * 3)
print("5 * 4 = ", 5 * 4)
print("5 * 5 = ", 5 * 5)
```

**Example: Multiplication Table of 5 (with loop, 1 to 10):**
```python
for i in range(1,11):
    print(f"5 * {i} = ", 5 * i)
```
_Output:_
```
5 * 1 =  5
5 * 2 =  10
...
5 * 10 =  50
```

**Example: Using `break` to stop the loop at i=6**
```python
for i in range(1,11):
    if i == 6:
        break
    print(f"5 * {i} = ", 5 * i)
```
_Output:_
```
5 * 1 =  5
5 * 2 =  10
...
5 * 5 =  25
```

**Example: Login Program with Limited Attempts**
```python
for i in range(1,5):
    user_name = input("Enter user id")
    user_password = input("Enter password")
    if (user_name == 'admin' and user_password == 'password'):
        print("Login success")
        break
    else:
        print("Login failed")
```

**Example: Using `continue` to skip a value**
```python
for i in range(1,11):
    if i == 6:
        continue
    print(f"5 * {i} = ", 5 * i)
```
_Skips printing the 6th multiplication line._

**Iterating over lists:**
```python
names = ["Pavan", "Ajay", "Amar", "Sanjay", "Vijay"]
for name in names:
    print(name, len(name))
```

**Iterating over dictionary keys:**
```python
student = {'name': 'Arun', 'age': 15, 'subject': 'Physics'}
for k in student:
    print(student[k])
```

---

## While Loop

The `while` loop is used when the number of iterations is not known in advance and you want to repeat a block until a condition becomes false.

**Example:**
```python
i = 0
while i <= 5:
    print(i, 'i is smaller then 5')
    i = i + 1
```
_Output:_
```
0 i is smaller then 5
1 i is smaller then 5
...
5 i is smaller then 5
```

**Example: Infinite Login Until Correct Credentials**
```python
while True:
    user_name = input("Enter user id")
    user_password = input("Enter password")
    if (user_name == 'admin' and user_password == 'password'):
        print("Login success")
        break
    else:
        print("Login failed")
```

---

## Filtering Numbers using Loops

**Finding all prime numbers between 1 and 100 (using for loop):**
```python
prime_numbers = []
for i in range(2,101):
    is_prime = True
    for k in range (2,(i//2) + 2):
        if i % k == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)
print(set(prime_numbers))
```

**Finding all prime numbers between 1 and 100 (using while loop):**
```python
prime_numbers = []
i = 2
while i < 101:
    is_prime = True
    for k in range (2,(i//2) + 2):
        if i % k == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)
    i = i+1
print(prime_numbers)
```

---

## User Defined Functions

Functions help with code reusability and organizing logic.

**Example: Function to add 7 to a number**
```python
def add_seven(x):
    print(x + 7)

add_seven(9)  # Output: 16
add_seven(2)  # Output: 9
add_seven(3)  # Output: 10
```

**Example: Function to add two numbers**
```python
def do_sum(x, y):
    print(x + y)

do_sum(9, 3)  # Output: 12
do_sum(7, 1)  # Output: 8
do_sum(4, 3)  # Output: 7
```

**Example: Function to calculate the square of a number**
```python
def calc_square(x):
    result = x**2
    print(result)

calc_square(9)  # Output: 81
calc_square(7)  # Output: 49
calc_square(3)  # Output: 9
```

---

## Exercises

- Filter and identify all even numbers between 0 and 100.
- Filter and identify all odd numbers between 0 and 100.

---

**Summary:**  
This document illustrated various looping constructs (`for`, `while`), control statements (`break`, `continue`), iteration over lists and dictionaries, and the basics of writing functions in Python, with practical code examples.
