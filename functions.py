from sklearn.metrics import accuracy_score, recall_score, f1_score, roc_auc_score


def metrics(y_test, predictions):
    """
    Takes the test labels and a model's predictions
    of the labels and prints the accuracy, recall, f1, and roc auc score.

    :param y_test: True labels
    :param predictions: Predicted Labels
    :return:
    """
    print(f'Accuracy: {(accuracy_score(y_test, predictions))}')
    print(f'Recall: {(recall_score(y_test, predictions))}')
    print(f'F1: {(f1_score(y_test, predictions))}')
    print(f'ROC AUC: {(roc_auc_score(y_test, predictions))}')
