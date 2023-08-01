#!/usr/bin/python3
"""A module that contains canUnlock all function"""


def canUnlockAll(boxes):
    """
    A function that checks if all the boxes can be unlocked.

    boxes: locked boxes that contain keys that may unlock other boxes
    """
    num_of_boxes = len(boxes)
    max_box_number = num_of_boxes - 1

    # Store useful unique keys in a set
    keys = {0}

    # Search the opened box for useful keys
    for key in boxes[0]:
        if key <= max_box_number:
            keys.add(key)

    # Unlock boxes
    while True:
        new_keys = set()  # Separate set to track new keys in this iteration
        for key in keys:
            for k in boxes[key]:
                if k <= max_box_number and k not in keys:
                    new_keys.add(k)
                    if len(keys) + len(new_keys) == num_of_boxes:
                        return True

        if not new_keys:
            break

        keys.update(new_keys)  # Update the keys set after this iteration

    return len(keys) == num_of_boxes