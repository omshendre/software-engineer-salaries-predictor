# Software Engineer Salaries Predictor

This project aims to predict the salaries of software engineers based on various factors such as country, education level, years of experience, and the year of the survey. The data used for this project was obtained from the Stack Overflow Developer Survey for the years 2021 and 2022.

## Data Preparation

To prepare the dataset for analysis, the data from both years was concatenated into a single dataset using the `ConcatDataset.ipynb` notebook. After that, the dataset was cleaned to remove any irrelevant or missing values.

## Feature Extraction

The required information for predicting the salary includes the following features: 
- Country: The country in which the software engineer resides.
- Education Level: The highest level of education attained by the software engineer.
- Years of Experience: The number of years of professional experience the software engineer has.
- Year: The year of the survey.

The target variable for prediction is the salary of the software engineer.

## Model Training

The DecisionTreeRegressor algorithm was used to train the prediction model. This algorithm is suitable for regression tasks and can handle both numerical and categorical features. The model was trained using the cleaned dataset.

## Model Storage

Once the model was trained, it was stored in the `.pkl` format for future use in the deployment of the application.

## App Deployment

For the deployment of the application, Streamlit was used. Streamlit is an open-source Python library that simplifies the creation and sharing of interactive web applications. The deployed application can be accessed at [software-engineer-salaries-predictor.streamlit.app](https://software-engineer-salaries-predictor.streamlit.app/).

## Required Packages

To run the project, the following packages are required:
- pandas
- matplotlib
- sklearn
- streamlit

### Installation Instructions

To install the required packages, please follow these instructions:

1. Make sure you have Python installed on your system. You can download it from the official Python website (https://www.python.org) and follow the installation instructions for your operating system.

2. Open a command prompt or terminal.

3. Run the following command to install the packages using pip:
   `pip install pandas matplotlib scikit-learn streamlit`
4. If you are using a conda environment, you can use the following command instead:
    `conda install pandas matplotlib scikit-learn streamlit`
    
