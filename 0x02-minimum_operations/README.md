# Minimum Operations

This script calculates the fewest number of operations needed to achieve a specific number of H characters in a text file.

## Description

In a text file, there is a single character H. The script provides a method `minOperations(n)` that calculates the minimum number of operations required to result in exactly `n` H characters in the file. The two available operations are:

1. Copy All: Copies all the characters in the file.
2. Paste: Pastes the copied characters at the end of the file.

The script implements a mathematical approach to find the minimum operations. It factors `n` and counts the factors as the number of operations.

## Example

```python
n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

Output:
```
Min # of operations to reach 9 char: 6
```