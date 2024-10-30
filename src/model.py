# src/model.py

from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import SplineTransformer
from sklearn.ensemble import VotingRegressor, StackingRegressor
from sklearn.linear_model import Ridge
import numpy as np

def get_models():
    """
    Returns a list of predefined models.
    """
    models = [
        ("Linear Regression", LinearRegression()),
        ("Elastic Net", ElasticNet()),
        ("Random Forest", RandomForestRegressor()),
        ("Gradient Boosting", GradientBoostingRegressor()),
        ("MLP Regressor", MLPRegressor())
    ]
    return models

def blend_models(models, X_train, X_val, y_train, y_val):
    """
    Fit each base model and use predictions as features for meta-model.
    """
    level_1_features = []
    for name, model in models:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        level_1_features.append(y_pred.reshape(-1, 1))
    
    level_1_features = np.hstack(level_1_features)
    meta_model = MLPRegressor()
    meta_model.fit(level_1_features, y_val)
    return meta_model, models

def get_stacking_model():
    """
    Returns a stacking model.
    """
    base_models = [
        ('Linear Regression', LinearRegression()),
        ('Gradient Boosting', GradientBoostingRegressor())
    ]
    meta_model = Ridge()
    stacking_model = StackingRegressor(estimators=base_models, final_estimator=meta_model)
    return stacking_model