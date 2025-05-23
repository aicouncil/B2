# Python Sequential Data Types: Strings

This document covers the key topics from the Jupyter notebook `el_python_d2.ipynb` regarding Python's sequential data type: the string. Each topic is explained with definitions, code examples, and detailed explanations.

---

## 1. **String: Definition and Properties**

A **string** in Python is a sequence of characters.  
- **Immutability**: Once created, the contents of a string cannot be changed.

**Example:**
```python
name = "Vinay Pratap Singh"
print(name)              # Output: Vinay Pratap Singh
print(type(name))        # Output: <class 'str'>
```

---

## 2. **Creating Strings**

Strings can be created using:
- Single quotes: `'Hello'`
- Double quotes: `"World"`
- Triple quotes for multi-line: `'''Multi\nLine'''`

**Example:**
```python
city = 'Delhi'
print(city)              # Output: Delhi

product_review = '''
The product i used
was really good and 
i want to recommend it to 
my friends and families
'''
print(product_review)
```

---

## 3. **Accessing Characters and Slices**

You can access individual characters and substrings using indexing and slicing.

**Indexing:**
```python
print(city[0])  # 'D'
print(city[1])  # 'e'
print(city[2])  # 'l'
print(city[-1]) # 'i' (last character)
print(name[13]) # 'S'
```

**Slicing:**
```python
print(name[13:18])   # 'Singh'
print(name[0:5])     # 'Vinay'
```

---

## 4. **String Length**

Get the number of characters with `len()`:
```python
print(len(name))     # 18
print(len(city))     # 5
print(len(product_review))  # Includes newlines and spaces
```

---

## 5. **String Operations**

### a. Splitting Strings
Use `split()` to divide a string into a list.
```python
print(name.split(' '))        # ['Vinay', 'Pratap', 'Singh']
print(product_review.split('\n'))
# ['', 'The product i used', 'was really good and ', 'i want to recommend it to ', 'my friends and families', '']
```

### b. Stripping Whitespace
- `strip()`: Removes whitespace from both ends
- `lstrip()`: Removes leading (left) whitespace
- `rstrip()`: Removes trailing (right) whitespace

```python
print(product_review.strip())
print(product_review.lstrip())
print(product_review.rstrip())
```

### c. Concatenation
Combine strings using `+` or `' '.join()`.

```python
first_name = "Bipul"
last_name = "Shahi"
print(first_name + " " + last_name)  # Bipul Shahi
print(' '.join([first_name, last_name]))  # Bipul Shahi
```

### d. Repetition
Repeat a string with `*`:
```python
print(first_name * 3)  # BipulBipulBipul
```

### e. Changing Case
- `upper()`: All uppercase
- `lower()`: All lowercase

```python
print(first_name.upper())  # 'BIPUL'
print(first_name.lower())  # 'bipul'
```

### f. Membership
Check if a substring exists in a string using `in`:
```python
print('good' in product_review.lower())  # True
```

### g. f-Strings (Formatted Strings)
Insert values into strings easily:
```python
name = 'Ajay'
age = 35
print(f"My name is {name} and I am {age} years old")
# Output: My name is Ajay and I am 35 years old
```

### h. Escape Characters
Special characters like newline (`\n`):
```python
print("Hello\nWorld")
# Output:
# Hello
# World
```

---

## 6. **String Immutability**

Strings cannot be changed in place.

```python
name = "Anil"
# name[0] = 'K'  # Error: 'str' object does not support item assignment

# To "change" a string, create a new one:
name = "Vinay Pratap Singh"
new_name = name.replace("Singh", "King")
print(new_name)  # Vinay Pratap King
```

---

## 7. **Summary Table: Common String Operations**

| Operation           | Example                          | Description                           |
|---------------------|----------------------------------|---------------------------------------|
| Indexing            | `city[0]`                        | First character                       |
| Slicing             | `name[0:5]`                      | Substring (positions 0 to 4)          |
| Length              | `len(name)`                      | Number of characters                  |
| Split               | `name.split(' ')`                | Split into list                       |
| Strip               | `product_review.strip()`         | Trim whitespace                       |
| Concatenation       | `first_name + last_name`         | Join strings                          |
| Repetition          | `first_name * 3`                 | Repeat string                         |
| Case                | `first_name.upper()`             | Uppercase                             |
| Membership          | `'good' in product_review`       | Substring check                       |
| f-strings           | `f"{name} {age}"`                | String interpolation                  |
| Replace             | `name.replace('Singh', 'King')`  | Replace substring                     |

---

## 8. **Key Points**

- Strings are immutable, sequential collections of characters.
- Strings support a variety of operations: slicing, splitting, joining, formatting, and more.
- Understanding string operations is fundamental for text processing in Python.

---
