# Python Day 7: Object-Oriented Programming (OOP) Concepts

This notebook covers foundational Object-Oriented Programming (OOP) concepts in Python, including how to define classes, create objects, use class and instance variables/methods, constructors, and access modifiers (`public` and `private`). Below you'll find explanations and examples for each major concept.

---

## 1. Variables and Functions Recap

Let's start with simple variable assignments and functions:

```python
name = "Arun"
print(name)
```
Output:
```
Arun
```

Addition example:
```python
x = 8
y = 3
z = x + y
print(z)
```
Output:
```
11
```

### Functions Returning Values

A function can return a value:

```python
def show_details(name, age):
    details = {'name': name, 'age': age}
    return details

show_details("Ajay", 12)
```
Output:
```
{'name': 'Ajay', 'age': 12}
```

### Functions Printing Output

A function can simply print a message:

```python
def show_details(name, age):
    print("hello World")

show_details("Joy", 23)
```
Output:
```
hello World
```

---

## 2. Object-Oriented Programming (OOP) Basics

### What is a Class?

- A class is a blueprint for creating objects.
- **Variables** in classes represent properties/attributes.
- **Functions** in classes (called methods) represent behaviors.

#### Minimal Class Example

```python
class MyClass:
    pass

obj1 = MyClass()  # Creating an object (instance) of MyClass
```

---

### Class Attributes and Methods

```python
class Vehicle:
    color = 'red'  # Class attribute

    def drive(self):  # Method
        return "120 km/h"

v1 = Vehicle()
print(v1.color)    # Output: red
print(v1.drive())  # Output: 120 km/h
```

**Explanation:**
- `color` is a property of the `Vehicle` class.
- `drive` is a method that describes behavior.
- `self` refers to the instance of the class.

---

### Instance Attributes and Methods

```python
class Employee:
    def emp_details(self):
        self.name = 'Ajay'
        self.age = 23

    def show_details(self):
        details = {'name': self.name, 'age': self.age}
        return details

e1 = Employee()
e1.emp_details()
print(e1.show_details())  # Output: {'name': 'Ajay', 'age': 23}
```

**Explanation:**  
Instance attributes like `self.name` and `self.age` are specific to each object created from the class.

---

### Parameterized Methods

You can pass values to methods to set properties:

```python
class Employee:
    def emp_details(self, e_name, e_age):
        self.name = e_name
        self.age = e_age

    def show_details(self):
        details = {'name': self.name, 'age': self.age}
        return details

e1 = Employee()
e1.emp_details('Pratik', 22)
print(e1.show_details())  # Output: {'name': 'Pratik', 'age': 22}
```

---

## 3. Class Variables and Counting Objects

Sometimes, you might want to keep track of the number of objects created:

```python
class Students:
    count = 0  # Class variable

    def student_details(self, name, standard):
        self.name = name
        self.class_studying = standard
        Students.count += 1

    def add_marks(self, marks):
        self.marks = marks

    def show_details(self):
        details = {'name': self.name, 'class': self.class_studying, 'marks': self.marks}
        return details

    def show_count(self):
        return Students.count

s1 = Students()
s1.student_details('Arun', '5th')
s1.add_marks(34)

s2 = Students()
s2.student_details('Amir', '4th')
s2.add_marks(32)

print(s1.show_details())  # Output: {'name': 'Arun', 'class': '5th', 'marks': 34}
print(s2.show_details())  # Output: {'name': 'Amir', 'class': '4th', 'marks': 32}
print(s1.show_count())    # Output: 2
```

---

## 4. Constructor (`__init__` Method)

The `__init__` method is called a constructor and is used to initialize new objects:

```python
class Students:
    def __init__(self, name, std):
        self.name = name
        self.standard = std

    def add_marks(self, marks):
        self.marks = marks
        if self.marks > 90:
            self.grades = 'A+'
        elif self.marks > 80:
            self.grades = 'A'
        elif self.marks > 70:
            self.grades = 'B'
        else:
            self.grades = 'C'

    def show_details(self):
        details = {'name': self.name, 'Standard': self.standard, 'Marks': self.marks, 'Grades': self.grades}
        return details

s1 = Students("Abhay", "6th")
s1.add_marks(80)
print(s1.show_details())
```

**Output:**
```
{'name': 'Abhay', 'Standard': '6th', 'Marks': 80, 'Grades': 'B'}
```

---

## 5. Access Modifiers: Public and Private Variables

In Python, variables prefixed with double underscores (`__`) are treated as private:

```python
class Students:
    def __init__(self, name, std):
        self.__name = name        # Private variable
        self.__standard = std     # Private variable

    def add_marks(self, marks):
        self.marks = marks
        if self.marks > 90:
            self.grades = 'A+'
        elif self.marks > 80:
            self.grades = 'A'
        elif self.marks > 70:
            self.grades = 'B'
        else:
            self.grades = 'C'

    def show_details(self):
        details = {'name': self.__name, 'Standard': self.__standard, 'Marks': self.marks, 'Grades': self.grades}
        return details

ps1 = Students("Abhay", "6th")
ps1.add_marks(80)
print(ps1.show_details())
```
**Output:**
```
{'name': 'Abhay', 'Standard': '6th', 'Marks': 80, 'Grades': 'B'}
```

#### Attempting to Access Private Variables Directly

```python
print(ps1.__name)
```
**Output/Error:**
```
AttributeError: 'Students' object has no attribute '__name'
```
**Explanation:**  
Private variables cannot be accessed directly from outside the class.

---

## 6. Summary Table

| Concept                 | Example Syntax                              | Description                                |
|-------------------------|---------------------------------------------|--------------------------------------------|
| Class Definition        | `class MyClass:`                            | Blueprint for objects                      |
| Object Creation         | `obj = MyClass()`                           | Create an instance of a class              |
| Instance Variable       | `self.name = value`                         | Variable unique to each object             |
| Class Variable          | `class_var = value`                         | Shared among all objects                   |
| Method                  | `def method(self):`                         | Function inside a class                    |
| Constructor             | `def __init__(self, ...):`                  | Initializes new objects                    |
| Public Variable         | `self.var = value`                          | Accessible from outside                    |
| Private Variable        | `self.__var = value`                        | Accessible only within class               |

---

## 7. Key Takeaways

- **Classes** group related data and functions.
- **Objects** are instances of classes.
- **self** lets methods access instance data.
- **Class variables** are shared; **instance variables** differ per object.
- **Constructors** (`__init__`) initialize new objects.
- Prefix variables with `__` to make them private.

---

## Practice Exercise

Try creating your own `Book` class with:

- A class variable for `total_books`
- Instance variables for `title`, `author`
- Methods to set details, display details, and show total books

---

Happy Coding!
