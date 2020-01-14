""" Akshay Lavhagale
    SSW 810 - Homework 06
    From part 1 to 5 try to implement list comprehensions and in part 6 sorting list in ascending order
"""


# Part 1: list_copy(l)
def list_copy(l):
    """ take a list as a parameter and returns a copy of the list """
    return [x for x in l]


# Part 2: list_intersect(l1, l2)
def list_intersect(l1, l2):
    """ takes two lists as  parameters and returns a new list with the values that are included in both lists """
    return [value for value in l1 if value in l2]


# Part 3: list_difference(l1, l2)
def list_difference(l1, l2):
    """ takes two lists as  parameters and returns a new list with the values that are  in l1, but not in l2 """
    return [value for value in l1 if value not in l2]


# Part 4: remove_vowels(string)
def remove_vowels(string):
    """ returns a copy of the string with no vowels """
    return ''.join([c for c in string if c not in 'aeiouAEIOU'])


# Part 5: Password checker check_pwd(password)
def check_pwd(password):
    """ take a string as a parameter, checks whether it includes all three parameters and returns a boolean value """
    if any([item.isupper() for item in password]) and any([item.islower() for item in password]) and (password[-1].
                                                                                                      isdigit()):
        return True
    else:
        return False


# Part 6: insertion_sort(l)
def insertion_sort(l):
    """ returns a copy of the argument sorted using a list and the insertion sort algorithm """
    """ we are going to start with empty list """
    sorted_list = []
    for item in l:
        """ we will start from offset 0 and will add element through insert function """
        offset = 0
        while offset < len(sorted_list) and item > sorted_list[offset]:
            offset += 1
        sorted_list.insert(offset, item)
    return sorted_list

'''
def insertion_sort(l):
    """ we are going to start with empty_list """
    list = []
    for item in l:
        """ we will start from offset 0 and will add element in list through enumerate """
        for offset, element in enumerate(list):
            """ if new item we are adding is less than the element already present """
            if item < element:
                """ then we are adding new item at offset position before element already present in list """
                list.insert(offset, item)
                break
        else:
            """ if value of item we are adding is more than already present element in list then item > element """
            list.append(item)
    return list
'''