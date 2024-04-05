"""Core module for main program logic."""

from src.utils import compare_characters, max_row_length


def define_file_content(filename: str) -> list[list[str]]:
    """Define the file's content in the form of a nested list.

    Each element in the list is a row from the file. White space is
    added to the file content, where needed, to create a matrix-like
    structure.

    Returns the file content as a nested list
    """
    # Open file
    with open(filename) as file:
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


def bug_sample_check(bug: list[list[str]], test_sample: list[list[str]]) -> list[bool]:
    """Check if the bug array and the test sample array are the same.

    White spaces in the bug are ignored. It returns a list with `True`
    or `False` for each character.
    """
    return [
        compare_characters(bug[i][j], test_sample[i][j])
        for i in range(len(bug))
        for j in range(len(bug[i]))
    ]


def find_bugs(
    bug_file_content: list[list[str]],
    test_file_content: list[list[str]],
) -> int:
    """Find number of bugs in test file."""
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
