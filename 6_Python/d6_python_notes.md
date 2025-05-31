# Exception Handling in Python

Exception handling is a critical concept in Python that allows programmers to deal with errors or unexpected situations gracefully, improving the robustness and maintainability of code. This document provides a comprehensive overview of exception handling, with explanations and examples inspired by the `el_python_d6.ipynb` notebook.

---

## 1. What is Exception Handling?

**Exception handling** is the process of responding to the occurrence of exceptions—errors detected during execution. Instead of letting errors crash the program, Python provides a way to catch and handle these exceptions, allowing the program to continue or exit gracefully.

### Why do we need Exception Handling?

- To prevent abrupt program termination.
- To provide meaningful error messages.
- To manage unforeseen situations (like missing files or invalid input).
- To make debugging and maintenance easier.

---

## 2. Basic Exception Handling with `try` and `except`

The simplest form of exception handling uses the `try` and `except` blocks.

```python
try:
    # Code that may raise an exception
    print(x)
except Exception as err:
    # Code that runs if an exception occurs
    print(err)
```

**Output:**
```
name 'x' is not defined
```

**Explanation:**  
Here, since `x` is not defined, a `NameError` occurs. The `except` block catches the error and prints its message.

---

## 3. Catching Specific Exceptions

You can catch specific types of exceptions for more precise error handling.

### Example: Catching `FileNotFoundError`

```python
try:
    myfile = open('file10.txt', 'r')
    print(myfile.read())
    myfile.close()
except FileNotFoundError:
    print("The file you are trying to open does not exist.")
```

**Output:**
```
The file you are trying to open does not exist.
```

### Example: Catching Multiple Exceptions

```python
try:
    myfile = open('file2.txt', 'r')
    myfile.write("Hello World")
    myfile.close()
except FileNotFoundError:
    print("The file you are trying to open does not exist.")
except IOError:
    print("Mode chosen and operation defined are different.")
```

**Output:**
```
Mode chosen and operation defined are different.
```

---

## 4. Using `else` and `finally` Clauses

- `else`: Executes if no exception occurs in the `try` block.
- `finally`: Executes no matter what, whether an exception occurred or not.

### Example:

```python
try:
    myfile = open('file2.txt', 'r')
except FileNotFoundError:
    print("The file you are trying to open does not exist.")
except IOError:
    print("Mode chosen and operation defined are different.")
else:
    print(myfile.read())
    myfile.close()
finally:
    print("All process done")
```

**Output (when file exists):**
```
Python Programming is for lazy programmers like Python reptile
I like the rain most.
Rabbit runs faster but turtle wins race.
All process done
```

**Output (when file does not exist):**
```
The file you are trying to open does not exist.
All process done
```

---

## 5. The `pass` Statement in Exception Handling

`pass` is used as a placeholder when no action is required.

```python
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
```

---

## 6. Handling Different Exception Types

You can handle different types of exceptions separately for more granular control.

```python
try:
    print(x)
except NameError:
    print('You are calling a non-defined variable')
```

**Output:**
```
You are calling a non-defined variable
```

---

## 7. Handling User Input with Exceptions

### Example: Validating Number Input

```python
while True:
    try:
        x = float(input("Please enter a number: "))
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
        break
    else:
        print(x)
```

**Example Run:**
```
Please enter a number: 4
4.0
Please enter a number: abcde
Oops! That was not a valid number. Try again...
```

---

## 8. Using `raise` to Trigger Exceptions

You can raise exceptions manually using the `raise` keyword.

```python
age = float(input("Enter your Age"))
if age > 18:
    raise Exception("Age is more than the threshold")
```

**Output:**
```
Exception: Age is more than the threshold
```

---

## 9. Nested Exception Handling and Type Conversion

Sometimes user input needs to be converted to a specific type, which might fail.

```python
age = input("Enter your Age")
try:
    print(age > 18)
except TypeError:
    try:
        print(float(age) > 18)
    except Exception as err:
        print(err)
```

---

## 10. Practical Example: BMI Calculator with Exception Handling

Let's create a program to calculate BMI, handling all possible exceptions:

### BMI Categories

- Underweight: BMI below 18.5
- Healthy weight: BMI between 18.5 and 24.9
- Overweight: BMI between 25.0 and 29.9
- Obesity: BMI of 30.0 or greater

### Formula

BMI = weight (kg) / [height (m)]²

### Example Implementation

```python
def calc_bmi(weight, height):
    try:
        bmi = weight / height**2
        if bmi <= 0:
            raise Exception("Weight or height can't be zero or negative")
        else:
            return bmi
    except TypeError:
        try:
            bmi = float(weight) / float(height)**2
            if bmi <= 0:
                raise Exception("Weight or height can't be zero or negative")
            else:
                return bmi
        except ValueError:
            return "Invalid data input"
        except ZeroDivisionError:
            return "Can't divide by zero"
```

**Using the function:**

```python
weight = input("Enter your weight in kgs: ")
height = input("Enter your height in m: ")

try:
    bmi = calc_bmi(weight, height)
    print(bmi)
except Exception as err:
    print(err)
```

---

## 11. Summary / Best Practices

- Always anticipate possible errors, especially with user input and file operations.
- Use specific exception types to catch only expected errors.
- Use `else` for code that should run if no errors occur.
- Use `finally` for cleanup actions that must run regardless of success or failure.
- Avoid using bare `except:` unless you have a good reason.
- Use meaningful error messages to help users and yourself debug problems.

---

## Conclusion

Exception handling is a vital part of writing robust and user-friendly Python programs. By using `try`, `except`, `else`, `finally`, and `raise`, you can gracefully handle errors, validate input, and ensure your program manages unexpected situations smoothly.

---
