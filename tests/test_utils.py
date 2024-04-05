"""Unit tests for utilities functions."""

from src.utils import compare_characters, max_row_length


def test_max_row_length() -> None:
    assert max_row_length([["a"], ["b", "c"]]) == 2


def test_compare_characters() -> None:
    assert compare_characters("a", "a")
    assert compare_characters(" ", "a")
    assert not compare_characters("a", " ")
    assert not compare_characters("a", "A")
