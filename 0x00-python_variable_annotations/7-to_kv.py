#!/usr/bin/env python3
"""
Module contains a function that returns a tuple with a string a
square of a number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int/float and returns a tuple with first element is
    a string and the second element is the square of the int/float
    and is a float.

    Args:
        k: (str): The string.
        v (Union[int, float]): The number to be squared.

        Returns:
            Tuple[str, float]: A string and the square of the number.
    """
    return k, v**2
