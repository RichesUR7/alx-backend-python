
dule contains a function that returns the first elements of a
sequence if itt exist.
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Takes a sequence as an argument and returns the first element if it
    exists, otherwise returns None.

    Args:
        lst (Sequence[Any]): The sequence.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]

    return None
