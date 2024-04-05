"""Unit tests for core functions."""

from src.core import (
    bug_sample_check,
    create_test_sample,
    define_file_content,
    find_bugs,
)


def test_define_file_content() -> None:
    expected = [
        ["|", " ", "|", "\n", " "],
        ["#", "#", "#", "O", "\n"],
        ["|", " ", "|", "\n", " "],
    ]
    actual = define_file_content("tests/bug_files/bug.txt")
    assert actual == expected


def test_create_test_sample() -> None:
    test_file_content = [[" ", "#", "O", "#", " "]]
    expected = [["O", "#"]]
    actual = create_test_sample(0, 2, 1, 2, test_file_content)
    assert actual == expected


def test_bug_sample_check() -> None:
    assert bug_sample_check([["O", "#"]], [["O", "#"]]) == [True, True]
    assert bug_sample_check([["O", "!"]], [["O", "#"]]) == [True, False]
    assert bug_sample_check([[" ", " "]], [["O", "#"]]) == [True, True]
    assert bug_sample_check([["O", "#"]], [[" ", " "]]) == [False, False]


def test_find_bugs_without_noise() -> None:
    bug_file_content = define_file_content("tests/bug_files/bug.txt")
    test_file_content = define_file_content("tests/test_files/test.txt")

    assert find_bugs(bug_file_content, test_file_content) == 3


def test_find_bugs_with_noise() -> None:
    bug_file_content = define_file_content("tests/bug_files/bug_small.txt")
    test_file_content = define_file_content("tests/test_files/test_with_noise.txt")

    assert find_bugs(bug_file_content, test_file_content) == 3
