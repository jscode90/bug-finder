"""Utilities module for general-purpose functions."""


def max_row_length(rows_list: list[list[str]]) -> int:
    """Return the length of the longest row list within rows_list.

    >>> max_row_length([["a"],["b", "c"]])
    2
    """
    return max([len(row) for row in rows_list])


def compare_characters(bug_char: str, test_char: str) -> bool:
    """Logic that compares two characters while ignoring white spaces.

    The white spaces are only ignored if present in `bug_char`

    >>> compare_characters("a", "A")
    False

    >>> compare_characters("a", " ")
    False

    >>> compare_characters(" ", "a")
    True
    """
    check_result = False
    if bug_char == test_char or bug_char.isspace():
        check_result = True
    return check_result
