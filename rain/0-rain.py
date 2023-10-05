#!/usr/bin/python3

"""
Given a list of non-negative integers representing the heights of walls
with unit width 1, as if viewing the cross-section of a relief map,
calculate how many square units of water will be retained after it rains.
"""
def calculate_rainwater(walls):
    """
    Calculate the total amount of rainwater that can be retained between walls.

    :param walls: A list of non-negative integers representing wall heights.
    :return: An integer indicating the total amount of retained rainwater.
    """

    # Check if there are any walls; if not, no water can be retained.
    if not walls:
        return 0

    # Initialize pointers for the leftmost and rightmost positions.
    left, right = 0, len(walls) - 1

    # Initialize variables to track the maximum heights from left and right.
    left_max, right_max = 0, 0

    # Initialize a variable to keep track of the total retained rainwater.
    retained_water = 0

    # Continue until the left pointer is less than the right pointer.
    while left < right:
        # If the left wall is shorter or equal to the right wall,
        if walls[left] <= walls[right]:
            # Update the left maximum height if needed.
            if walls[left] >= left_max:
                left_max = walls[left]
            # Calculate the water trapped at the left position and add it to retained_water.
            else:
                retained_water += left_max - walls[left]
            # Move the left pointer to the right.
            left += 1
        else:  # If the right wall is taller than the left wall,
            # Update the right maximum height if needed.
            if walls[right] >= right_max:
                right_max = walls[right]
            # Calculate the water trapped at the right position and add it to retained_water.
            else:
                retained_water += right_max - walls[right]
            # Move the right pointer to the left.
            right -= 1

    # Return the total retained rainwater.
    return retained_water

