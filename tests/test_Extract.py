import unittest
import spacy
import pandas as pd

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

    def test_gram_feats(self):
        inp = {'foo': [0,0], 'bar': [1,2]}
        test_df = pd.DataFrame(inp)
        shape = test_df.shape
        result = Extract.standardize(test_df)

        self.assertEqual(result.shape, shape)
        self.assertEqual(list(result.columns), ['bar', 'foo'])

        self.assertEqual(result.iloc[0].foo, 0)
        self.assertEqual(result.iloc[0].bar < result.iloc[1].bar, True)
