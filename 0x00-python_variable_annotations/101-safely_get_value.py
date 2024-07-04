#!/usr/bin/env python3
"""
Module contains a function that safely gets a value from a dictionary.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Takes a dictionary, a key, and a default value as arguments.
    If the key is in the dictionary, it returns the value of the key.
    Otherwise, it returns the default value.

    Args:
        dct (Mapping): The dictionary.
        key (Any): The key.
        default (Union[T, None]): The default value.

    Returns:
        Union[Any, T]: The value of the key in the dictionary if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]

    return default
