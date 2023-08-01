#!/usr/bin/python3
"""A module that contains canUnlock all function"""


def canUnlockAll(boxes):
    """
        A function that checks if all the boxes can be unlocked

            boxes: locked boxes that contain keys that may unlock other boxes
    """
    num_of_boxes = len(boxes)
    max_box_number = num_of_boxes - 1

    # store useful unique keys in a set
    keys = {0}

    # search the opened box for useful keys
    for key in boxes[0]:
        if key <= max_box_number:
            keys.add(key)

    # unlock boxes
    for i in range(1, num_of_boxes):
        if i < len(keys):
            key = list(keys)[i]
        for k in boxes[key]:
            if k <= max_box_number:
                keys.add(k)
        if len(keys) == max_box_number:
            return True
    return False
