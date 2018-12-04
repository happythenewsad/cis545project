import unittest
import spacy

from Extract import Extract


class Tester(unittest.TestCase):

    def test_feats(self):
        spacy_model = spacy.load('en_core_web_sm')
        text = "the quick brown fox!"
        result = Extract.feats(text, spacy_model)
        expected = {'sent_len': 20, 'NOUN_count': 1, 
          'ADV_count': 0, 'VERB_count': 0, 'ADJ_count': 2, 
          'PUNCT_count': 1, 'adv_verb_ratio': 0, 
          'adj_noun_ratio': 0.5, 'DET_count': 1,
          'colon_count': 0, 'semicolon_count': 0, 
          'lparen_count': 0, 'ellipse_count': 0, 'quote_count': 0, 
          'bang_count': 1}

        self.assertEqual(result, expected)
