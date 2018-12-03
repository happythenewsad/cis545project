import unittest

from Eval import Eval


class Tester(unittest.TestCase):

    def test_get_accuracy(self):
        y_pred = ['a', 'a', 'b', 'b']
        y_actual = ['a', 'b', 'a', 'b']
        result = Eval.get_accuracy(y_pred, y_actual);

        self.assertEqual(.5, result)
