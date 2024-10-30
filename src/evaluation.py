# src/evaluation.py

from sklearn.metrics import r2_score

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the model on the test data and returns the R2 score.
    """
    y_pred = model.predict(X_test)
    return r2_score(y_test, y_pred)