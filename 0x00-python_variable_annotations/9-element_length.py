#!/usr/bin/env python3
"""
Module contains a function the returns a list of tuples with
elements and their lengths.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences as an argument and returns a list of tuples.
    Each tuple contains a sequence from the iterable and its length.

    Args:
        lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples. Each tuple contains a
        sequence from the iterable and its length.
    """
    return [(i, len(i)) for i in lst]
