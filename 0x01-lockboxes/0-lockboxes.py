#!/usr/bin/python3
"""
Module: lockboxes
Contains the canUnlockAll function for checking if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    n = len(boxes)
    unlocked = [False] * n  # Track the unlocked status of each box
    unlocked[0] = True  # The first box is initially unlocked
    keys = boxes[0]  # Start with the keys from the first box

    while keys:
        key = keys.pop()  # Get a key from the list

        if not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])  # Add the keys from the opened box

    return all(unlocked)
