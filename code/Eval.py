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


    @staticmethod
    def nn_accuracy(classes, preds, Y):
        label_lookup = {}
        for idx, label in enumerate(classes):
            label_lookup[idx] = label
        label_lookup

        def best_label(row, lookup):
            mx = max(row)
            return lookup[list(row).index(mx)]

        preds = [best_label(x, label_lookup) for x in preds]

        accuracy = Eval.get_accuracy(preds, Y)
        print("NN Accuracy: ", accuracy)   