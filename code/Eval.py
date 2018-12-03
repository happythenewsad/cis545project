class Eval:


    @staticmethod
    def get_accuracy(y_pred, y_true):
        if len(y_pred) != len(y_true):
            raise ValueError("input sizes do not match!")

        vals = {'correct': 0, 'incorrect': 0}

        for idx in range(len(y_pred)):
            if y_pred[idx] == y_true[idx]:
                vals['correct'] += 1
            else:
                vals['incorrect'] += 1

        return vals['correct'] / (vals['correct'] + vals['incorrect'])


