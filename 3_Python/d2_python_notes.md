# Python Basics: Data Types, Operators, and Conditional Programming

This guide summarizes foundational Python concepts including dictionaries, booleans, sets, typecasting, operators, and introduces conditional programming. Each topic is explained with examples.

---

## 1. Dictionaries

- **Definition:** Collections of key-value pairs.
- **Use:** Efficiently store and retrieve data by key.

```python
student = {'name': 'Arun', 'age': 15, 'subject': 'Physics'}
print(student['name'])  # Output: Arun
```

- **Common Operations:**
  - Access keys: `student.keys()`
  - Access values: `student.values()`
  - Add item: `student['marks'] = 55.7`
  - Update value: `student['age'] = 14`
  - Remove item: `student.pop('age')`

---

## 2. Booleans

- **Definition:** Represents `True` or `False` values.
- **Use:** Logical operations and control flow.

```python
status = True
print(type(status))  # Output: <class 'bool'>
```

---

## 3. Sets

- **Definition:** Unordered collections of unique items.
- **Use:** Remove duplicates, membership tests.

```python
unique_ids = {'a12', 'a13', 'b25', 'c72', 'd43'}
unique_ids.add('c79')
print(unique_ids)
```

- **Note:** Sets cannot be indexed or sliced (not subscriptable).

---

## 4. Typecasting

- **Definition:** Converting a variable from one type to another.

```python
a = 56.9
b = int(a)     # 56
c = str(a)     # '56.9'
d = list([b])  # [56]
```

- **Conversions:**
  - `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`

---

## 5. Operators in Python

### Arithmetic Operators

| Operator | Description           | Example  |
|----------|-----------------------|----------|
| +        | Addition              | a + b    |
| -        | Subtraction           | a - b    |
| *        | Multiplication        | a * b    |
| /        | Division (float)      | a / b    |
| **       | Exponentiation        | a ** b   |
| //       | Floor Division        | a // b   |
| %        | Modulus (remainder)   | a % b    |

```python
a = 17
b = 5
print(a + b)  # 22
print(a ** b) # 1419857
```

### Assignment Operators

| Operator | Example     | Equivalent      |
|----------|-------------|----------------|
| =        | x = 10      | x = 10         |
| +=       | x += 2      | x = x + 2      |
| -=       | x -= 3      | x = x - 3      |
| *=       | x *= 4      | x = x * 4      |
| /=       | x /= 5      | x = x / 5      |
| **=      | x **= 2     | x = x ** 2     |
| //=      | x //= 3     | x = x // 3     |
| %=       | x %= 5      | x = x % 5      |

### Comparison Operators

| Operator | Description      | Example      |
|----------|------------------|-------------|
| ==       | Equal to         | age == 18   |
| >        | Greater than     | age > 10    |
| <        | Less than        | age < 15    |
| >=       | Greater or equal | age >= 17   |
| <=       | Less or equal    | age <= 17   |
| !=       | Not equal        | age != 18   |

### Logical Operators

| Operator | Description      | Example            |
|----------|------------------|--------------------|
| and      | Logical AND      | a > 5 and b < 10   |
| or       | Logical OR       | a > 5 or b < 3     |
| not      | Logical NOT      | not(a > 5)         |

### Membership Operators

| Operator | Description      | Example           |
|----------|------------------|-------------------|
| in       | Value present    | 3 in [1,2,3,4]    |
| not in   | Value not present| 5 not in [1,2,3]  |

---

## 6. Conditional Programming

Conditional programming allows execution of code based on certain conditions using `if`, `elif`, and `else` statements.

### Syntax

```python
if condition:
    # code if condition is True
elif another_condition:
    # code if another_condition is True
else:
    # code if none above are True
```

### Example

```python
age = 18
if age > 18:
    print("You are an adult.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are not an adult.")
```

---

## 7. Practical Examples: Combining Concepts

```python
student = {'name': 'Arun', 'age': 17, 'marks': 85}
if student['marks'] > 80:
    print("Distinction")
else:
    print("Keep trying!")
```

---

## Summary

- **Dictionaries** store data as key-value pairs.
- **Booleans** represent truth values.
- **Sets** hold unique, unordered elements.
- **Typecasting** converts between data types.
- **Operators** perform arithmetic, assignment, comparison, and logic.
- **Conditional programming** executes code based on conditions.

Explore these core Python concepts to build a strong programming foundation!
