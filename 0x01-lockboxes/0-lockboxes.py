#!/usr/bin/python3
"""lock boxes"""


def canUnlockAll(boxes):
    """checking locked and unlocked boxes"""
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    i = 0
    while i < len(unlocked):
        current_box = unlocked[i]
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
        i += 1

    if len(unlocked) == len(boxes):
        return True
    else:
        return False
