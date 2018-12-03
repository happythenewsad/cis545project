import unittest

from Eval import Eval


class Tester(unittest.TestCase):

    def test_tp_tn_fp_fn(self):
        y_pred = [1,1,0,0]
        y_actual = [1,0,1,0]
        result = Eval.tp_tn_fp_fn(y_pred, y_actual);

        self.assertEqual(1, result['tp'])
        self.assertEqual(1, result['fp'])
        self.assertEqual(1, result['tn'])
        self.assertEqual(1, result['fn'])