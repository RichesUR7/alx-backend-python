#!/usr/bin/env python3
"""
Module contains a function that sums a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats nad returns their sum as float.

    Args:
        mxd_lst (List[Union[int,float]]): List of integers and floats.

    Returns:
        float: Sum of integers and floats.
    """
    return sum(mxd_lst)
