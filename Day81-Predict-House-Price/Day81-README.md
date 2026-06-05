# Day 81 – Multivariable Regression & House Valuation Model 🏠📈

An end-to-end Data Science project focused on predicting Boston housing prices using statistical hypothesis testing,
advanced data transformation, and Multivariable Linear Regression modeling.

## Key Workflow & Features

- **Data Exploration & Cleaning:** Analyzed the Boston Housing dataset, checked for missing values, and explored
  features like structural characteristics (RM) and socio-economic factors (LSTAT).
- **Statistical Hypothesis Testing:** Conducted two-sample T-Tests (using `scipy.stats`) to rigorously validate the
  impact of proximity to the Charles River (`CHAS`) on property values.
- **Data Transformation (Log Regression):** Addressed the right-skewed distribution of housing prices by applying a Log
  Transformation to the target variable to satisfy OLS assumptions.
- **Model Training & Evaluation:** Implemented a clean pipeline using `scikit-learn` to split data into Train/Test sets,
  fit a Multiple Linear Regression model, and evaluate performance using $R^2$ scores and residual analysis.
- **Property Valuation Predictor:** Created a flexible simulation interface to estimate property values based on custom
  parameters (e.g., crime rates, room counts, and pupil-teacher ratios).

## Tech Stack

- Python 3
- **Pandas & NumPy:** Data manipulation, feature engineering, and matrix operations.
- **Matplotlib & Seaborn:** Statistical data visualization, correlation heatmaps, and residual plotting.
- **Scikit-Learn:** Data splitting (`train_test_split`) and Linear Regression modeling.
- **SciPy:** Advanced statistical calculations and T-test execution.

## How to Run

1. Install the required data science dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy notebook