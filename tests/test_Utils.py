import unittest
from nltk.stem.porter import PorterStemmer
import spacy

from Utils import Utils



class Tester(unittest.TestCase):
    def test_tokenize(self):
        inp = 'Words, words, words.'
        expected = ['words', 'words', 'words']
        self.assertEqual(Utils.tokenize(inp), expected)

        inp = 'why? just because; i said.'
        expected = ['why', 'just', 'because', 'said']
        self.assertEqual(Utils.tokenize(inp), expected)

    def test_stem_n_stop(self):
        stemmer = PorterStemmer()
        nlp = spacy.load('en_core_web_sm')
        result = Utils.stem_n_stop("Jerry's quick brown apple apples", nlp, stemmer)
        expected = ["jerri", "'s", "quick", "brown", "appl", "appl"]
        self.assertEqual(result, expected)

