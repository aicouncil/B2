# Numpy Concepts Explained

This document summarizes and explains the concepts covered in the notebook `el_ds_1(numpy).ipynb`. Each section includes explanations and illustrative examples (in Python) to help you understand the core topics.

---

## 1. Python Lists vs Numpy Arrays

### Python Lists
- **Heterogeneous:** Lists can store elements of different types.
- **Example:**
    ```python
    salaries = [30000, 40000, 20000, 10000, 15000]
    print(salaries * 2)
    # Output: [30000, 40000, 20000, 10000, 15000, 30000, 40000, 20000, 10000, 15000]
    ```
    List multiplication repeats the list.

- **Heterogeneous Example:**
    ```python
    l1 = [3, 2, 6, 7.1, 'abc']
    print(l1)
    # Output: [3, 2, 6, 7.1, 'abc']
    ```

### Numpy Arrays
- **Homogeneous:** All elements must be of the same type.
- **Efficient mathematical operations.**
- **Example:**
    ```python
    import numpy as np
    salary = np.array([30000, 40000, 20000, 10000, 15000])
    print(salary * 2)
    # Output: [60000 80000 40000 20000 30000]
    ```
    Array multiplication scales each element.

---

## 2. Numpy Array Creation and Types

- **Basic Array:**
    ```python
    n1 = np.array([3, 5, 6, 7, 8])
    print(n1)
    # Output: [3 5 6 7 8]
    ```

- **Homogeneous Types:**
    ```python
    n2 = np.array([3, 5.1, 6, 7, 8])
    print(n2)
    # Output: [3.  5.1 6.  7.  8. ]
    ```
    If any element is a float, all values become floats.

- **Strings in Array:**
    ```python
    n3 = np.array([3, 5.1, '6', 7, 8])
    print(n3)
    # Output: ['3' '5.1' '6' '7' '8']
    ```

---

## 3. Array Dimensions, Shape, and Type

- **1D Array:**
    ```python
    print(n1.ndim)  # Output: 1
    print(n1.shape) # Output: (5,)
    ```

- **2D Array:**
    ```python
    n2 = np.array([[2, 3, 5, 6, 7] , [3, 2, 6, 7, 9] , [4, 3, 17, 6, 3]])
    print(n2.ndim)  # Output: 2
    print(n2.shape) # Output: (3, 5)
    ```

---

## 4. Numpy Mathematical and Statistical Functions

Given an array `n2`:
```python
n2 = np.array([[2, 3, 5, 6, 7],
               [3, 2, 6, 7, 9],
               [4, 3, 17, 6, 3]])
```

- **Aggregate Functions:**
    ```python
    np.sum(n2)    # Sum of all elements
    np.prod(n2)   # Product of all elements
    np.mean(n2)   # Mean of all elements
    np.min(n2)    # Minimum value
    np.max(n2)    # Maximum value
    np.std(n2)    # Standard deviation
    np.argmin(n2) # Index of min value (flattened)
    np.argmax(n2) # Index of max value (flattened)
    ```

- **Axis-wise Operations:**
    - **Rows (axis=1):**
        ```python
        np.sum(n2, axis=1)    # Sum for each row
        np.min(n2, axis=1)    # Min for each row
        ```
    - **Columns (axis=0):**
        ```python
        np.sum(n2, axis=0)    # Sum for each column
        np.max(n2, axis=0)    # Max for each column
        ```

---

## 5. Indexing and Slicing

### Indexing
- **Accessing Elements:**
    ```python
    print(n2[2, 3])   # Access element at row 2, column 3
    # Output: 6
    ```

- **Finding Indices:**
    ```python
    np.where(n2 == 9)
    # Output: (array([1]), array([4]))
    ```

### Slicing
- **1D Array Slicing:**
    ```python
    n1 = np.array([3,4,6,7,2,7,1,9,5])
    print(n1[3:8])    # Output: [7 2 7 1 9]
    ```

- **2D Array Slicing:**
    ```python
    print(n2[1:4, 0:4])   # Rows 1-3, columns 0-3
    print(n2[:, 8:])      # All rows, columns 8 to end
    print(n2[-1, :])      # Last row
    print(n2[:, -2:])     # Last two columns
    ```

---

## 6. Broadcasting

Broadcasting allows numpy to perform operations on arrays of different shapes:

- **Scalar Broadcasting:**  
  Adding a scalar to an array applies the operation to every element.
    ```python
    n3 = np.array([[3,2,6,1], [2,4,1,6], [3,5,2,7]])
    print(n3 + 7)
    # Output:
    # [[10  9 13  8]
    #  [ 9 11  8 13]
    #  [10 12  9 14]]
    ```

- **Row-wise Broadcasting:**  
  Add a list (length matches number of columns) to each row.
    ```python
    l = [3, 1, 2, 1]
    print(n3 + l)
    # Output:
    # [[ 6  3  8  2]
    #  [ 5  5  3  7]
    #  [ 6  6  4  8]]
    ```

- **Column-wise Broadcasting:**  
  Add a column vector (shape matches number of rows) to each row.
    ```python
    col = np.array([[1], [2], [3]])
    print(n3 + col)
    # Output:
    # [[ 4  3  7  2]
    #  [ 4  6  3  8]
    #  [ 6  8  5 10]]
    ```

- **Shape Rules:**  
  Broadcasting works if:
    - Arrays have the same shape, or
    - One of them is 1 in a dimension (e.g., (3, 4) and (3, 1)), or
    - It’s a scalar.

---

## 7. Summary Table

| Concept                | List                 | Numpy Array            |
|------------------------|----------------------|------------------------|
| Data Types             | Heterogeneous        | Homogeneous            |
| Mathematical Ops       | Not Element-wise     | Element-wise           |
| Slicing                | Supported            | Supported              |
| Broadcasting           | Not Supported        | Supported              |
| Performance            | Slower               | Faster (Vectorized)    |

---

## 8. Key Takeaways

- Use **lists** for simple, small, or heterogeneous data.
- Use **numpy arrays** for large, numerical, and homogeneous data—especially when you need efficient computation.
- Numpy enables powerful operations like broadcasting, axis-based calculations, and fast vectorized math.

---

## References

- [Numpy Documentation](https://numpy.org/doc/)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
