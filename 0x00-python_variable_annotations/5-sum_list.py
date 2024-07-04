#!/usr/bin/env python3
"""
Module contains a function that sums a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats and returns their sum as a float.

    Args:
        input_list (List[float]): List of floats.
        Returns:
            float: Sum of the floats in the lisrt.
    """
    return sum(input_list)
