import unittest
from nltk.stem.porter import PorterStemmer
import spacy

from Utils import Utils



class Tester(unittest.TestCase):
    def test_test(self):
        self.assertEqual(False, False)

    def test_stem_n_stop(self):
        stemmer = PorterStemmer()
        nlp = spacy.load('en_core_web_sm')
        result = Utils.stem_n_stop("Jerry's quick brown apple apples", nlp, stemmer)
        expected = ["jerri", "'s", "quick", "brown", "appl", "appl"]
        self.assertEqual(result, expected)

