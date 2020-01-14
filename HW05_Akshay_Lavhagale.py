""" Akshay Lavhagale
    SSW 810 - Homework 05
    String methods and automated testing """


# Part 1: reverse(str)
def reverse(str):
    """ Function that takes a string as an argument and returns a new string which is the reverse of the argument """
    new_string = ''
    index = len(str)
    while index:
        """ index = index - 1 """
        index -= 1
        """ new_string = new_string + character """
        new_string += str[index]
    return new_string


# Part 2: rev_enumerate(seq)
def rev_enumerate(seq):
    """ Write a generator that return the elements in the sequence from last to first with the corresponding offset """
    count = len(seq) - 1
    for offset in reversed(seq):
        yield count, offset
        count -= 1


# Part 3: find_second(target, string)
def find_second(s1, s2):
    """ Returns the offset of the second occurrence of s1 in s2. As string.find method accepts an optional
        second argument, finds the first occurrence beginning at offset 1 rather than offset 0 """
    second_occ = s2.find(s1, s2.find(s1) + 1)
    return second_occ


# Part 4: get_lines(path)
def get_lines(file_path):
    """ First combine lines that end with a backslash (a continuation) with the subsequent line or lines until
        a line is found that does not end with a backslash. Remove all comments starting with '#' """
    try:
        """ Giving the correct encoding, the BOM is omitted in the result """
        fp = open(file_path, 'r', encoding='utf-8-sig')
    except FileNotFoundError:
        raise FileNotFoundError("Please check the file name you wish to open")
    else:
        """ with fp: whatever we open it closes once we done with it """
        with fp:
            for line in fp:
                """ line = strip the \n from the end of the line """
                line = line.rstrip("\n")
                while line.endswith("\\"):
                    """ merge continued lines """
                    line = line[:-1] + fp.readline().rstrip('\n')
                if line.startswith("#"):
                    """ ignore this line.  Go back for the next line """
                    continue
                elif "#" in line:
                    """ yield the line up to, but not including the '#' """
                    s1 = line.find("#")
                    yield line[:s1]
                else:
                    yield line


print(list(get_lines('test1.txt')))