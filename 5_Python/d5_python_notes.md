# Summary of Topics Covered in `el_python_d5.ipynb`

This notebook explores various aspects of **Python functions**, including their definitions, types of arguments, lambda functions, and practical examples. This summary provides explanations and code snippets for each covered topic.

---

## 1. Functions in Python

**Functions** are reusable blocks of code that perform a specific task. They help in organizing code, avoiding repetition, and improving readability.

### Example: Calculating Square of a Number

```python
def calc_square(x):
    result = x ** 2
    print(result)
```

---

## 2. Login Function Example

A basic function that checks user credentials:

```python
def login(user_name, user_password):
    if (user_name == 'admin' and user_password == 'password'):
        print("Login success")
    else:
        print("Login failed")
```

**Usage:**
```python
login('admin', 'abcde')      # Output: Login failed
login('admin', 'password')   # Output: Login success
```

**Interactive Example:**
```python
user_name = input("Enter user id")
user_password = input("Enter password")
login(user_name, user_password)
```

---

## 3. Leap Year Checker Function

A leap year is:
- Divisible by 4,
- Not divisible by 100 unless also divisible by 400.

### Example Function

```python
def check_leap(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print(year, "is leap year")
    else:
        print(year, "is not leap year")
```

### To Get All Leap Years in a Range

```python
leap_years = []
for year in range(1900, 2001):
    if check_leap(year):
        leap_years.append(year)
print(leap_years)
```

---

## 4. Returning Values from Functions

A function can return a value using the `return` statement.

```python
def do_sum(x, y):
    return x + y

result_1 = do_sum(6, 3)
print(result_1)       # Output: 9
print(result_1 * 2)   # Output: 18
```

---

## 5. Default Parameters

Functions can have default values for arguments.

```python
def users_detail(name, age='NA', weight='NA'):
    details = {"Name": name, "Age": age, "Weight": weight}
    return details

users_detail("Ajay", 23)                 # {'Name': 'Ajay', 'Age': 23, 'Weight': 'NA'}
users_detail("Ajay")                     # {'Name': 'Ajay', 'Age': 'NA', 'Weight': 'NA'}
users_detail("Ajay", 23, 55)             # {'Name': 'Ajay', 'Age': 23, 'Weight': 55}
users_detail(age=23, weight=55, name="Ajay")  # keyword arguments
```

---

## 6. Variable Length Arguments

### Positional Arguments (`*args`)

Allows a function to accept any number of positional arguments as a tuple.

```python
def calculate_sum(*args):
    total_sum = 0
    for arg in args:
        total_sum += arg
    return total_sum

print(calculate_sum(8, 3, 2, 1))  # Output: 14
print(calculate_sum(8, 3, 2))     # Output: 13
print(calculate_sum(8, 3))        # Output: 11
```

---

### Keyword Arguments (`**kwargs`)

Allows a function to accept any number of keyword arguments as a dictionary.

```python
def user_details(**kwargs):
    entered_details = {}
    for key, value in kwargs.items():
        entered_details[key] = value
    return entered_details

user_details(name='Atul')                           # {'name': 'Atul'}
user_details(name='Atul', age=23)                   # {'name': 'Atul', 'age': 23}
user_details(name='Ajith', age=45, city='Chennai')  # {'name': 'Ajith', 'age': 45, 'city': 'Chennai'}
```

---

## 7. Lambda Functions

**Lambda functions** are small anonymous functions defined using the `lambda` keyword. They are useful for simple, one-line operations.

### Example: Product of Two Values

```python
multiplication = lambda x, y: x * y
multiplication(3, 2)  # Output: 6
multiplication(9, 3)  # Output: 27
```

### Example: Square of a Number

```python
_square = lambda x: x * x
_square(9)  # Output: 81
```

### Example: Even or Odd

```python
evens = lambda num: "even" if num % 2 == 0 else "odd"
evens(6)  # Output: 'even'
evens(7)  # Output: 'odd'
```

### Example: Lambda for Login Check

```python
login = lambda user_name, user_password: "Login success" if user_name == 'admin' and user_password == 'password' else "Login failed"
login('admin', 'password')  # Output: 'Login success'
login('admin', 'passwor')   # Output: 'Login failed'
```

### Example: Lambda for Leap Year

```python
leap = lambda year: (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
print(leap(2000))  # Output: True
print(leap(2002))  # Output: False

if leap(2000):
    print("it is leap year")
else:
    print("it is not a leap year")
```

---

## Conclusion

This notebook covers the essentials of Python functions:
- Defining and calling functions
- Using return values
- Default parameters
- Variable-length arguments (`*args`, `**kwargs`)
- Lambda (anonymous) functions

These concepts are foundational for writing efficient, modular, and reusable Python code.
