""" Akshay Lavhagale
    Homework 07 - Python Containers
    The goal of this assignment is to give you a chance to practice using list, tuple, dictionary, and set """


import unittest
from HW07_Akshay_Lavhagale import anagram_lst, anagrams_dd, anagrams_cntr, covers_alphabet, book_index


class TestContainer(unittest.TestCase):
    def test_anagram_lst(self):
        """ Function that returns True if str1 and str2 are anagrams, False if not, using only list. """
        self.assertEqual((anagram_lst("car", "tree")), False)
        self.assertNotEqual((anagram_lst("car", "tree")), True)
        self.assertEqual((anagram_lst("Iceman", "Cinema")), True)
        self.assertEqual((anagram_lst("ICEMAN", "CINEMA")), True)
        self.assertEqual((anagram_lst("", "")), True)
        self.assertEqual((anagram_lst("iceman", "iceman ")), False)
        self.assertEqual((anagram_lst('123', '321')), True)

    def test_anagrams_dd(self):
        """ Determine if two strings are anagrams using defaultdict """
        self.assertEqual((anagrams_dd("DORMITORY", "DIRTYROOM")), True)
        self.assertNotEqual((anagrams_dd("Cinema", "Iceman")), False)
        self.assertEqual((anagrams_dd("car", "Tree")), False)
        self.assertEqual((anagrams_dd("", "")), True)
        self.assertEqual((anagrams_dd('123', '321')), True)

    def test_anagrams_cntr(self):
        """ Determine if two strings are anagrams using only collections.Counters"""
        self.assertEqual((anagrams_cntr("Dormitory", "Dirtyroom")), True)
        self.assertNotEqual((anagrams_cntr("car", "tree")), True)
        self.assertEqual((anagrams_cntr("iceman", "cinema")), True)
        self.assertEqual((anagrams_cntr("", "")), True)
        self.assertEqual((anagrams_cntr('123', '321')), True)

    def test_covers_alphabet(self):
        """ returns True if sentence includes at least one instance of every character in the alphabet or False """
        self.assertEqual((covers_alphabet("AbCdefghiJklomnopqrStuvwxyz")), True)
        self.assertNotEqual((covers_alphabet("xyz")), True)
        self.assertEqual((covers_alphabet("We promptly judged antique ivory buckles for the next prize")), True)
        self.assertEqual((covers_alphabet("abcdefghijklmnopqrstuvwxyz")), True)
        self.assertEqual((covers_alphabet("aabbcdefghijklmnopqrstuvwxyzzabc")), True)
        self.assertEqual((covers_alphabet("The quick brown fox jumps over the lazy dog")), True)
        self.assertEqual((covers_alphabet("")), False)

    def test_book_index(self):
        """ A book index lists all of the words in the book along with a unique list of pages where that word occurs """
        expected = [['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]], ['much', [3]],
                    ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]]
        woodchucks = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1), ('chuck', 3),
                      ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
        result = book_index(woodchucks)
        self.assertEqual(result, expected)

        expected_1 = [['word1', [1, 3]], ['word2', [2]]]
        sentence_1 = [('word1', 1), ('word2', 2), ('word1', 1), ('word1', 3)]
        result_1 = book_index(sentence_1)
        self.assertEqual(result_1, expected_1)

        expected_2 = [['word1', [1, 3]], ['word2', [2]]]
        sentence_2 = [('word1', 1), ('word2', 2), ('word1', 1), ('word1', 4)]
        result_2 = book_index(sentence_2)
        self.assertNotEqual(result_2, expected_2)

        self.assertEqual(book_index([]), [])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)  # these are the parameters and will use help(unittest.main)
