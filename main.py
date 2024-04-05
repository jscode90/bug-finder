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

from src.core import define_file_content, find_bugs

if __name__ == "__main__":
    # 1. Extract file content for the bug and test files
    bug_file_content = define_file_content("tests/bug_files/bug.txt")
    test_file_content = define_file_content("tests/test_files/test.txt")

    # 2. Perform bug count
    bug_count = find_bugs(bug_file_content, test_file_content)
    print(f"A total of {bug_count} bugs were found!")  # noqa: T201
