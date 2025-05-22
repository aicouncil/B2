# Python Basics: Quick Start Guide

Welcome! This guide will help you get started with Python using simple examples.

---

## 1. Printing Output

Use `print()` to display output:

```python
print("Hello World")
```
_Output:_
```
Hello World
```

---

## 2. Variables and Values

Variables store data values.

```python
name = "Bipul"
age = 32
city = "Delhi"
```

You can print multiple values together:

```python
print(name, age, city)
```
_Output:_
```
Bipul 32 Delhi
```

You can assign values in one line:

```python
a, b, c = 9, 6, 3
print(a, b, c)
```
_Output:_
```
9 6 3
```

Assign the same value to multiple variables:

```python
x = y = z = 1234
print(x)
print(y)
print(z)
```
_Output:_
```
1234
1234
1234
```

---

## 3. Data Types

- **String**: Text data (e.g., `"Vinay"`)
- **Integer**: Whole numbers (e.g., `32`)
- **Float**: Decimal numbers (e.g., `3065.34`)
- **Complex**: Numbers with real and imaginary parts (e.g., `3 + 5j`)

Examples:

```python
name = "Bipul"
print(type(name))  # <class 'str'>

age = 32
print(type(age))   # <class 'int'>

salary = 3065.34
print(type(salary))  # <class 'float'>

complex_number = 3 + 5j
print(type(complex_number))  # <class 'complex'>
```

---

## 4. Basic Operations

Python can do arithmetic easily:

```python
a = 9
b = 2
result = a * b
print(result)
```
_Output:_
```
18
```

---

## 5. Strings and Indexing

Strings are sequences of characters. You can access characters by their position (index):

```python
name = "Vinay Pratap Singh"
print(name[0])  # V
print(name[1])  # i
print(name[2])  # n
```

---

## 6. What’s Next?

Other important topics you will learn in Python:

- Data Types & Data Structures
- Operators
- Conditional Programming
- Loops
- Functions
- Exception Handling

---

Feel free to use and edit this guide in your project!
