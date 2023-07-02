# Pascal's Triangle

This repository contains a Python function `pascal_triangle(n)` that generates the Pascal's triangle of size `n`. The Pascal's triangle is a triangular array of binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it.

## Function Signature

```python
def pascal_triangle(n):
    ...
```

## Usage

The function `pascal_triangle(n)` takes an integer `n` as input and returns a list of lists representing the Pascal's triangle of size `n`. If `n` is less than or equal to 0, an empty list is returned.

To print the Pascal's triangle, you can use the `print_triangle` function provided in the `0-main.py` file. Here's an example:

```python
from 0-pascal_triangle import pascal_triangle, print_triangle

# Generate Pascal's triangle of size 5
triangle = pascal_triangle(5)

# Print the triangle
print_triangle(triangle)
```

This will output the following:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## Example

```python
from 0-pascal_triangle import pascal_triangle, print_triangle

# Generate Pascal's triangle of size 7
triangle = pascal_triangle(7)

# Print the triangle
print_triangle(triangle)
```

Output:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
```

