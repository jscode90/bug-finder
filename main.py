"""Main file which runs logic to find bugs.

@author: Juan Sebastian Gutierrez Gomez
@title: Find The Bug

The logic behind the solution to this problem is the following:

1)  Define the contents of the bug file and the test file
    with a 2D array (matrix) using nested lists.

2)  With the correspondent dimensions of the bug matrix and the test
    matrix, one can define how many bugs could fit in the test matrix,
    therefore, a scan of all possible places where the bug could be can
    be done.

3)  Test samples, with the same size of the bug matrix, are taken
    from the test matrix at each possible position. Then they are
    compared with the bug matrix for a match.

4)  Each test sample goes through a series of checks where the bug
    pattern has to be identical and white spaces are treated specially
    as they don't make part of the bug pattern, allowing for a noisy
    background.

Example:
    Bug  ->   o#o
         ->   this can be seen as a 1x3 array   ->  |o|#|o|

    Test ->   x  o
              xxo#ox
         ->   this can be seen as a 2x6 array   ->  |x| |o| | | |
                                                    |x|x|o|#|o|x|

The scanning is done comparing the 'bug array' vs 'test sample array',
for every possible position where the bug might be:

   ITER    BUG        SAMPLE    MATCH
    1.   |o|#|o| vs. |x| |o| -> False
    2.   |o|#|o| vs. | |o| | -> False
    3.   |o|#|o| vs. |o| | | -> False
    .
    .
    .
    7.   |o|#|o| vs. |o|#|o| -> True
    .
    .
    .
   20.   |o|#|o| vs. |x| | | -> False

"""


def max_row_length(rows_list: list[list[str]]) -> int:
    """Return the length of the longest row list within rows_list.

    >>> max_row_length([["a"],["b", "c"]])
    2
    """
    return max([len(row) for row in rows_list])


def define_file_content(file_name: str) -> list[list[str]]:
    """Define the file's content in the form of a nested list.

    Each element in the list is a row from the file. White space is
    added to the file content, where needed, to create a matrix-like
    structure.

    Returns the file content as a nested list
    """
    # Open file
    with open(file_name) as file:
        # Create the nested list with the file's content
        file_content = [list(line) for line in file]

    # Define the longest row length
    max_len = max_row_length(file_content)

    # Add white spaces to the rows when needed
    for row in file_content:
        if len(row) < max_len:
            add_col = max_len - len(row)
            for _ in range(add_col):
                row.append(" ")

    return file_content


def compare_characters(bug_char: str, test_char: str) -> bool:
    """Logic that compares two characters while ignoring white spaces.

    >>> compare_characters("a", "A")
    False

    >>> compare_characters("a", " ")
    True
    """
    check_result = False
    if bug_char == test_char or bug_char.isspace():
        check_result = True
    return check_result


def bug_sample_check(bug: list[list[str]], test_sample: list[list[str]]) -> list[bool]:
    """Check if the bug array and the test sample array are the same.

    White spaces in the bug are ignored.It returns a list with `True`
    or `False` for each character.
    """
    return [
        compare_characters(bug[i][j], test_sample[i][j])
        for i in range(len(bug))
        for j in range(len(bug[i]))
    ]


def create_test_sample(
    i: int,
    j: int,
    i_bug_size: int,
    j_bug_size: int,
    test_file_content: list[list[str]],
) -> list[list[str]]:
    """Create a bug-sized array from the test file content at (i,j) position.

    Returns the test sample as a nested list.
    """
    return [
        [test_file_content[row_idx][col_idx] for col_idx in range(j, j + j_bug_size)]
        for row_idx in range(i, i + i_bug_size)
    ]


def bug_count_check(
    bug_file_content: list[list[str]],
    test_file_content: list[list[str]],
) -> int:
    """Check the numbers of bugs in the test file."""
    # Define bug size
    i_bug_size = len(bug_file_content)
    j_bug_size = len(bug_file_content[0])

    # Define possible checks in horizontal and vertical direction
    i_size = len(test_file_content) - len(bug_file_content)
    j_size = len(test_file_content[0]) - len(bug_file_content[0])

    # Check count
    check_count = 0
    for i in range(i_size + 1):
        for j in range(j_size + 1):
            # Create test sample for the (i,j) position in the array
            test_sample = create_test_sample(
                i,
                j,
                i_bug_size,
                j_bug_size,
                test_file_content,
            )

            # Compare bug with test sample
            final_check = bug_sample_check(bug_file_content, test_sample)

            # If all checks are truthful, a bug is found!
            if all(final_check):
                check_count += 1

    return check_count


if __name__ == "__main__":
    # 1. Format file content for both the bug and the test file
    bug_file_content = define_file_content("tests/bug.txt")
    test_file_content = define_file_content("tests/test.txt")

    # 2. Perform bug count
    bug_count = bug_count_check(bug_file_content, test_file_content)
    print(f"A total of {bug_count} bugs were found!")  # noqa: T201
