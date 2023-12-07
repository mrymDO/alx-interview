#!/usr/bin/python3
"""lock boxes"""


def canUnlockAll(boxes):
    """checking locked and unlocked boxes"""
    unlocked_boxes = set()

    boxes_to_check = [0]

    while boxes_to_check:
        current_box = boxes_to_check.pop()

        unlocked_boxes.add(current_box)

        for key in boxes[current_box]:
            if key not in unlocked_boxes:
                boxes_to_check.append(key)

    return len(unlocked_boxes) == len(boxes)
