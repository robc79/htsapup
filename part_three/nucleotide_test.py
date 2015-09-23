#! /usr/bin/env python3

# Unit tests for nucleotide.py module.

import unittest     # The unittest library.
import nucleotide   # The module to be tested.

class CountSequenceTest(unittest.TestCase):
    def setUp(self):
        # Called before running any test methods.
        pass


    def tearDown(self):
        # Called after running all test methods.
        pass


    def test_empty_sequence_gives_zero_totals(self):
        # arrange the data needed for testing
        empty_sequence = ""

        # call the count function with the test data
        totals = nucleotide.count(empty_sequence)

        # expectation is a 0 total for each nucleotide
        self.assertTrue([t for t in totals.values() if t != 0] == [],
            "Totals should be zero for empty sequence.")


    def test_lowercase_sequence_gives_correct_totals(self):
        sequence = "acgt"   # test all symbols in lowercase
        totals = nucleotide.count(sequence)
        self.assertTrue([t for t in totals.values() if t != 1] == [],
            "Lowercase a,c,g,t should be recognised as valid input.")




class ParseSequenceArgumentTest(unittest.TestCase):
    def setUp(self):
        # Called before running any test methods.
        pass


    def tearDown(self):
        # Called after running all test methods.
        pass




class ShowTotalsTest(unittest.TestCase):
    def setUp(self):
        # Called before running any test methods.
        pass


    def tearDown(self):
        # Called after running all test methods.
        pass




if __name__ == "__main__":
    # Run all tests when the module is invoked as a script.
    unittest.main()
