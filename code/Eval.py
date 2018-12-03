class Eval:

    @staticmethod
    def get_precision(y_pred, y_true):
        vals = tp_tn_fp_fn(y_pred, y_true)
        return vals['tp'] / (vals['tp'] + vals['fp'])


    @staticmethod
    def get_recall(y_pred, y_true):
        vals = tp_tn_fp_fn(y_pred, y_true)
        return vals['tp'] / (vals['tp'] + vals['fn'])

    @staticmethod
    def get_fscore(y_pred, y_true):
        precision = get_precision(y_pred, y_true)
        recall = get_recall(y_pred, y_true)

        return 2 * precision * recall / (precision + recall)

    @staticmethod
    def get_performance(y_pred, y_true):
        precision = get_precision(y_pred, y_true)
        recall = get_recall(y_pred, y_true)
        fscore = get_fscore(y_pred, y_true)

        return [precision, recall, fscore]

    @staticmethod
    def print_performance(performance):
        precision = performance[0]
        recall = performance[1]
        fscore = performance[2]
        print("precision, recall, fscore: ")
        [print(" {0}".format(x)) for x in [precision, recall, fscore]]


    # Helper for get_precision and get_recall
    @staticmethod
    def tp_tn_fp_fn(y_pred, y_true):
        if len(y_pred) != len(y_true):
            raise ValueError("input sizes do not match!")

        vals = {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}

        for idx in range(len(y_pred)):
            if (y_pred[idx] == 1 and y_true[idx] == 1):  # tp
                vals['tp'] += 1
            elif (y_pred[idx] == 1 and y_true[idx] == 0):  # fp
                vals['fp'] += 1
            elif (y_pred[idx] == 0 and y_true[idx] == 1):  # fn
                vals['fn'] += 1
            else:  # tn
                vals['tn'] += 1
        return vals
