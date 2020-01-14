""" Akshay Lavhagale
    Homework 07 - Python Containers
    The goal of this assignment is to give you a chance to practice using list, tuple, dictionary, and set. """


from collections import defaultdict
from collections import Counter


# Part 1: Anagrams
# Part 1.1: anagram_lst(str1, str2) Anagrams using only strings and lists
def anagram_lst(str1, str2):
    """ Function that returns True if str1 and str2 are anagrams, False if not, using only list. """
    return sorted(str1.lower()) == sorted(str2.lower())


# Part 1.2: anagrams_dd(str1, str2) Anagrams using defaultdict
def anagrams_dd(str1, str2):
    """ Determine if two strings are anagrams using defaultdict """
    """ when a key isn't present it'll substitute in a default value rather than raising a KeyError """
    freq1 = defaultdict(int)
    freq2 = defaultdict(int)
    str1 = str1.lower()
    str2 = str2.lower()
    for char in str1:
        freq1[char] += 1
    for char in str2:
        freq2[char] += 1

    return freq1 == freq2


# Part 1.3: anagrams_cntr(str1, str2) Anagrams using Counters
def anagrams_cntr(str1, str2):
    """ Determine if two strings are anagrams using only collections.Counters"""
    # make dictionaries from both strings
    return Counter(str1.lower()) == Counter(str2.lower())


# Part 2: covers_alphabet(sentence)
def covers_alphabet(sentence):
    """ returns True if sentence includes at least one instance of every character in the alphabet or False """
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    """ Converting the input string to lower case before comparing """
    string = set(sentence.lower())
    """ The issuperset() method returns True if a set has every elements of another set (passed as an argument) """
    return string.issuperset(alphabet)
    # return set(s.lower()) >= set("abcdefghijklmnopqrstuvwxyz") - one line of code


# Part 3: book_index(words) Book index
def book_index(words):
    """ A book index lists all of the words in the book along with a unique list of pages where that word occurs"""
    """ defaultdict - takes no arguments and provides the default value for a nonexistent key """
    dictonary1 = defaultdict(set)
    for key, value in words:
        dictonary1[key].add(value)
    return [[words, sorted(dictonary1[words])] for words in sorted(dictonary1.keys())]
