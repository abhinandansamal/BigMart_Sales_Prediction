# src/tuning.py

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.neural_network import MLPRegressor

def tune_stacking_model(stacking_model, X_train, y_train):
    """
    Hyperparameter tuning for the stacking model.
    """
    param_grid = {
        'final_estimator__alpha': [0.1, 1.0, 10.0],
        'final_estimator__fit_intercept': [True, False]
    }
    grid_search = GridSearchCV(stacking_model, param_grid, scoring='r2', cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_