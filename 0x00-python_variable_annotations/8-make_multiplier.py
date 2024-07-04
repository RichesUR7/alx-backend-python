#!/usr/bin/env python3
"""
Module contains a function that returns a function that
multiplies a float by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float and returns a function that multiplies
    a float by the given multiplier.

    Args:
        multiplier (float): The multiplier.

    Returns:
    Callable[[float], float]: A function that multiplies
    a float by the given multiplier.
    """

    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
