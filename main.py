"""
@author: Juan Sebastian Gutierrez Gomez
@title: Finding The Bug

The logic behind the solution to this problem was the following:

1)  Define the contents of the bug file and the test file
    with a 2D array (matrix) using nested lists

2)  With the correspondent dimensions of the bug matrix and the test
    matrix, one can define how many bugs could fit in the test matrix,
    therefore, a scan of all possible places where the bug could be can
    be done

3)  Test samples, with the same size of the bug matrix, are taken
    from the test matrix at each possible position. Then they are
    compared with the bug matrix for a match

4)  Each test sample goes through a series of checks where the bug pattern
    has to be identical and white spaces are treated specially as they don't
    make part of the bug pattern, allowing for a noisy background

Example:

    Bug  ->   o#o      ->   this can be seen as a 1x3 array   ->  |o|#|o|

              x  o                                                |x| |o| | | |
              xxo#ox                                              |x|x|o|#|o|x|
    Test ->     xo     ->   this can be seen as a 5x6 array   ->  | | |x|o| | |
               oxx#                                               | |o|x|x|#| |
               ##x                                                | |#|#|x| | |

Then the scanning is done comparing the 'bug array' vs 'test sample array',
for every possible position where the bug might be:

   ITER    BUG        SAMPLE     MATCH
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

def bug_file():
    """Function to specify the bug's file name"""
    print("1) We need to specify the name of the bug file")
    print("Please do not forget to include its extension, e.g. -> bug.txt")
    while True:
        try:
            bug_name = input("Please enter the bug file's name:\n")
            with open(bug_name,'r') as file:
                pass
        except FileNotFoundError:
            print('An error has occurred! No such file exists. Please try again!')
            continue
        else:
            break
    return bug_name


def test_file():
    """Function to specify the test's file name"""
    print("2) We need to specify the name of the test file")
    print("Please do not forget to include its extension, e.g. -> landscape.txt")
    while True:
        try:
            test_name = input("Please enter the landscape file's name:\n")
            with open(test_name,'r') as file:
                pass
        except FileNotFoundError:
            print('An error has occurred! No such file exists. Please try again!')
            continue
        else:
            break
    return test_name


def char_split(word):
    """Returns a list with every single character in a word
    e.g. 'hello' -> ['h','e','l','l','o']"""
    return [char for char in word]


def max_length(lst):
    """Returns the lenght of the longest list within lst"""
    return max([len(i) for i in lst])


def define_file_content(file_name):
    """Defines the file's content in the form of a nested list,
    each element in the list is a row from the file

    White space is added to the file content, when needed, to create
    a matrix-like structure

    Returns the file content as a nested list"""

    #Open file
    with open(file_name,'r') as file:
        file_content = []

        #This part creates the nested list with the file's content
        for line in file:
            file_content.append(char_split(line))

    #Here we define the longest row length
    max_len = max_length(file_content)

    #Here white spaces are added to the rows when needed
    for row in file_content:
        if len(row) < max_len:
            add_col = max_len - len(row)
            for i in range(add_col):
                row.append(' ')

    return file_content


def bug_check(bug_char,test_char):
    """Logic that compares two characters, white spaces are ignored
    returns True or False"""
    check_result = False
    if bug_char == test_char or bug_char.isspace():
        check_result = True
    return check_result


def bug_sample_check(bug,test_sample):
    """Checks if the bug array and the sample array from the test
    are identical (ignoring white spaces of the bug)
    returns a list with True or False for each character check done"""
    sample_check = []
    for i in range(0,len(bug)):
        for j in range(0,len(bug[i])):
            sample_check.append(bug_check(bug[i][j],test_sample[i][j]))
    return sample_check


def sample_test(i,j,test_content,y_bug_size,x_bug_size):
    """Creates a squared bug-sized array from the test content matrix
    at position i and j, returns the test sample as a nested list"""
    test_sample = []
    for a in range(i,i+y_bug_size):
        row = []
        for b in range(j,j+x_bug_size):
            row.append(test_content[a][b])
        test_sample.append(row)
    return test_sample


def bug_count_test(bug_content,test_content):
    """Checks the numbers of bugs found in the test file
    returns it as an int value"""

    #Definition of bug size
    y_bug_size = len(bug_content)
    x_bug_size = len(bug_content[0])

    #Definition of number of possible checks in horizontal and vertical direction
    ver_size = len(test_content)-len(bug_content)
    hor_size = len(test_content[0])-len(bug_content[0])

    #Check count
    check_count = 0
    for i in range(0,ver_size+1):
        for j in range(0,hor_size+1):
            #Creation of test sample for position i and j from the content
            test_sample = sample_test(i,j,test_content,y_bug_size,x_bug_size)

            #Comparison of bug with test sample
            final_check = bug_sample_check(bug_content, test_sample)

            #If all checks are truthful, a bug was found
            if all(final_check):
                check_count += 1

    return check_count


if __name__ == '__main__':
    #1. Bug file name definition
    bug_file_name = bug_file()
    #bug_file_name = "bug.txt"

    #2. Test file name definition
    test_file_name = test_file()
    #test_file_name = "test.txt"

    #3. Format file content for both the bug and the test files
    bug_file_content = define_file_content(bug_file_name)
    test_file_content = define_file_content(test_file_name)

    #4. Bug count
    bug_count = bug_count_test(bug_file_content,test_file_content)
    print("A total of "+str(bug_count)+" bugs were found!")
