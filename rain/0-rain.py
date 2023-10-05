#!/usr/bin/python3

"""
Given a list of non-negative integers representing the heights of walls
with unit width 1, as if viewing the cross-section of a relief map,
calculate how many square units of water will be retained after it rains.

Prototype: def rain(walls)
walls is a list of non-negative integers.
Return: Integer indicating total amount of rainwater retained.
Assume that the ends of the list (before index 0 and after index walls[-1]) are
not walls, meaning they will not retain water.
If the list is empty return 0.

"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    :param walls: A list of non-negative integers representing wall heights.
    :return: Integer indicating the total amount of rainwater retained.
    """

    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if walls[left] <= walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                water += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                water += right_max - walls[right]
            right -= 1

    return water
