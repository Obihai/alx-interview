# Lockboxes

This project contains a Python module called `lockboxes` that provides a function to determine if all the boxes can be opened in a given set of locked boxes.

---

## Installation

No installation is required for this module. Simply import the `lockboxes` module into your Python script.

---

## Usage

```python
from lockboxes import canUnlockAll

# Example usage
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
```

The `canUnlockAll` function takes a list of lists `boxes` as an argument and returns `True` if all the boxes can be opened, or `False` otherwise.
