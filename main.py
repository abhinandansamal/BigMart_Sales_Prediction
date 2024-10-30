# main.py

from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.feature_engineering import feature_engineering
from src.model import get_models, blend_models, get_stacking_model
from src.evaluation import evaluate_model
from src.tuning import tune_stacking_model
from sklearn.model_selection import train_test_split

# Load data
data = load_data()

# Preprocess data
data = preprocess_data(data)

# Feature Engineering
data = feature_engineering(data)

# Split data
X = data.drop(columns=["item_outlet_sales"])
y = data["item_outlet_sales"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Stacking Model
stacking_model = get_stacking_model()
stacking_model = tune_stacking_model(stacking_model, X_train, y_train)
print("Stacking Model R2:", evaluate_model(stacking_model, X_test, y_test))

# Train Blending Model
X_train_split, X_val_split, y_train_split, y_val_split = train_test_split(X_train, y_train, test_size=0.1, random_state=42)
meta_model, base_models = blend_models(get_models(), X_train_split, X_val_split, y_train_split, y_val_split)
print("Blending Model R2:", evaluate_model(meta_model, X_test, y_test))