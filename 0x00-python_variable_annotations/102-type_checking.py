#!/usr/bin/env python3
"""
This module contains a function that zooms in on a list.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Takes a tuple and an integer as arguments, and returns a list where
    each element of the tuple is repeated a number of times
    equal to the integer.

    Args:
        lst (Tuple): Tuple to be zoomed in on.
        factor (int): The number of times each element of the tuple should be
        repeated. Defaults to 2.

    Returns:
        List: A list where each element of the tuple is repeated a number of
        times equal to the integer.
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
