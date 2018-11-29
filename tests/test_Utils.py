import unittest
from Utils import Utils

import spacy

class Tester(unittest.TestCase):
    def test_vulgar(self):
        # this path param is relative to test_runner.py

        self.assertEqual(False, False)

    def test_stem_n_stop(text):
        nlp = spacy.load('en_core_web_sm')
        result = Utils.stem_n_stop("quick brown apple apples", nlp)
        print(result)

