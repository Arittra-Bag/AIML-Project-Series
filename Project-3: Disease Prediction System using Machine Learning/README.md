# Disease Prediction System using Machine Learning

## Overview

This project implements a Disease Prediction System using Machine Learning. It utilizes a RandomForestClassifier to predict diseases based on symptoms provided by the user.

## Dataset

The dataset used for training the model is available in two files:

- `Training.csv`: Contains the training data with symptoms and corresponding diseases.
- `Testing.csv`: Contains the testing data for evaluating the model.

## Dependencies

Make sure you have the following dependencies installed:

```bash
pip install pandas scikit-learn ipywidgets
```

## Usage

1. Open the Jupyter Notebook or Google Colab where you want to run the system.

2. Load the training dataset:

    ```python
    import pandas as pd

    # Load the training dataset
    df = pd.read_csv('/path/to/Training.csv')
    ```

3. Train the RandomForestClassifier model (replace with your actual training logic):

    ```python
    from sklearn.ensemble import RandomForestClassifier

    # Assuming X_train and y_train are your training features and labels
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    ```

4. Create an interactive dropdown interface:

    ```python
    from sklearn.preprocessing import LabelEncoder
    from ipywidgets import interact_manual, Dropdown

    # Exclude 'prognosis' from the symptom list
    symptoms = df.columns[:-1].tolist()

    # Encode the 'prognosis' column using LabelEncoder
    label_encoder = LabelEncoder()
    df['prognosis'] = label_encoder.fit_transform(df['prognosis'])

    # Create a function to make predictions based on selected symptoms
    def predict_disease(**selected_symptoms):
        # ... (use the provided code for this function)

    # Create an interactive dropdown for each symptom excluding 'prognosis'
    interact_manual(predict_disease, **{symptom: Dropdown(options=[0, 1], description=symptom) for symptom in symptoms if symptom != 'prognosis'})
    ```

5. Run the interactive dropdowns, select symptom values, and view the predicted disease.
