# BigMart_Sales_Prediction

This project focuses on forecasting sales for products across various BigMart outlets, leveraging historical sales data, machine learning, and advanced regression techniques. Accurate sales predictions enable better inventory management, cash flow planning, and optimized use of resources within stores.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Description](#data-description)
- [Approach and Methodology](#approach-and-methodology)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Takeaways](#project-takeaways)
- [License](#license)


## Project Overview
BigMart Sales Prediction is a Data Science project aimed at predicting the annual sales for various products at BigMart outlets. This project provides a robust workflow for data processing, feature engineering, model training, evaluation, and model tuning. The goal is to help BigMart analyze the factors influencing product sales, enabling data-driven decisions and optimized sales strategies.

## Data Description
The dataset consists of sales records for 2013, covering 1559 products across 10 stores in different locations. The data includes both input and output variables, as detailed below:

### Key Variables
* **Item_Identifier**: Unique product ID
* **Item_Weight**: Weight of the product
* **Item_Fat_Content**: Fat content of the product (low fat or regular)
* **Item_Visibility**: % of display area allocated to the product
* **Item_Type**: Product category (e.g., Dairy, Soft Drink, Household)
* **Item_MRP**: Maximum Retail Price of the product
* **Outlet_Identifier**: Unique store ID
* **Outlet_Establishment_Year**: Year the store was established
* **Outlet_Size**: Size of the store (small, medium, high)
* **Outlet_Location_Type**: Type of city where the store is located (Tier 1, 2, or 3)
* **Outlet_Type**: Type of store (e.g., Grocery, Supermarket)
* **Item_Outlet_Sales**: Total sales for the product at the store (target variable)

For a detailed description of each variable, please refer to the [Data Dictionary](docs/Data_Dictionary.docx) document.


## Approach and Methodology
This project follows a comprehensive methodology from data extraction to model evaluation. Key steps include:

1. **Data Extraction and Preprocessing**:
    * Data retrieval from an Amazon Redshift database.
    * Cleaning and imputing missing values using SQL and Python.

2. **Exploratory Data Analysis (EDA)**:
    * Analyzing categorical and continuous data.
    * Correlation analysis using Pearson’s Correlation, Chi-squared Test, Cramer’s V Test, and One-way ANOVA.

3. **Feature Engineering**:
    * Encoding categorical variables.
    * Creating new features, such as outlet age.

4. **Modeling and Evaluation**:
    * Building and training various regression models, including Linear Regression, Elastic Net, Random Forest, Extra Trees, Gradient Boosting, and MLP Regressor.
    * Implementing advanced techniques, such as Splines, Voting, Stacking, and Blending.

5. **Hyperparameter Tuning**:
    * Using GridSearchCV to fine-tune models and improve predictive accuracy.

## Tech Stack
* **Programming Language**: Python
* **Libraries**:
    * Data Processing: `Pandas`, `NumPy`, `scikit-learn`
    * Database Connection: `redshift_connector`, `dotenv`
    * Machine Learning: `scikit-learn`, `MLP Regressor`, `SplineTransformer`
    * Visualization: `matplotlib`, `seaborn`
    * Saving Models: `joblib`

## Project Structure
The project is organized as follows:
```
BIGMART_SALES_PREDICTION/
├── .env/                       # Environment variables for database connection
├── docs                        # Data Description & Methodology Documents
├── src/
│   ├── data_loader.py          # Load data from Redshift
│   ├── preprocess.py           # Data cleaning and preprocessing
│   ├── feature_engineering.py  # Feature engineering and encoding
│   ├── model.py                # Model building and ensembling methods
│   ├── evaluation.py           # Model evaluation and R2 calculation
│   ├── visualization.py        # Exploratory data analysis and plotting
│   └── tuning.py               # Hyperparameter tuning with GridSearchCV
├── main.py                     # Main script to run the pipeline
├── requirements.txt            # Required libraries
└── output/                     # Folder to store model files
````

### Key Files
* `src/data_loader.py`: Loads data from Redshift using credentials from `.env`.
* `src/preprocess.py`: Handles data cleaning, transformation, and missing value imputation.
* `src/feature_engineering.py`: Encodes categorical variables and creates new features.
* `src/model.py`: Defines regression models and ensemble techniques.
* `src/evaluation.py`: Contains functions for model evaluation (R2 score).
* `src/visualization.py`: Visualizations for data exploration.
* `src/tuning.py`: Hyperparameter tuning for models using `GridSearchCV`.
* `main.py`: Orchestrates the full pipeline from data loading to model evaluation.

## Getting Started
### Prerequisites
1. **Python 3.8 or later**: Ensure you have Python installed.

2. **Environment Setup**: Place your Redshift credentials in the `.env` file in the following format:
    ```
    REDSHIFT_HOST=<your_host>
    REDSHIFT_DATABASE=<your_database>
    REDSHIFT_USER=<your_user>
    REDSHIFT_PASSWORD=<your_password>
    REDSHIFT_PORT=<your_port>
    ```

### Installation
1. **Clone the repository**:
    ```
    git clone https://github.com/abhinandansamal/BigMart_Sales_Prediction.git

    cd bigmart_sales_prediction

    ```
2. **Create virtual environment**:
    ```
    conda create --name myenv python=3.12
    ```

3. **Activate the virtual environment**:
    ```
    conda activate myenv
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage
1. **Run the main pipeline**: Execute the pipeline from main.py, which will automatically load, preprocess, engineer features, build models, and display the evaluation results.
    ```
    python main.py
    ```

2. **Model Output**:
    * The trained models are saved in the `output/` directory.
    * Models include a tuned stacking regressor (`best_stacking_model.pkl`) and blending model components (`meta_model.pkl`, `LR_model.pkl`, `GBR_model.pkl`).

3. **Evaluating Results**: After execution, R2 scores for each model will be printed to the console. Visualization results will be shown for exploratory analysis and model evaluation.

## Project Takeaways
From this project, you will gain experience in:
1. Building a predictive model for sales forecasting with machine learning.
2. Exploring data with Amazon Redshift and preprocessing it with SQL and Python.
3. Analyzing categorical data relationships using statistical tests.
4. Implementing feature engineering techniques to enhance model performance.
5. Training and evaluating advanced regression models, including ensemble methods like Stacking and Blending.
6. Applying hyperparameter tuning to optimize model performance.

## License
This project is licensed under the MIT License.

--------

With this setup, you're ready to perform sales forecasting for BigMart and gain insights into the key factors driving sales across various products and store locations. Enjoy exploring the data and refining your models!