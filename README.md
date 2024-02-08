# DPS AI Challenge 

This challenge is intended for Artificial Intelligence Engineer for Digital Product School

## Description 
This challenge consists of 3 tasks.

- **Mission 1:** Create an AI Model, Training  Visualizing the data.
- **Mission 2:** Publish source code & Deploy the model 
- **Mission 3:** Sending the URL of the task

## API
The app is deployed on Heroku: [DPS App](https://dps-app-09bb6ce17a11.herokuapp.com/)

The endpoint accepts a POST request with a JSON body:

```json
{
  "year" : 2021,
  "month" : 10
}
```
It return prediction in the following format:

```json
{
"prediction" : value
}
```

# Dataset
The data represents the number of accidents for specific categories per month. Important are the first 5 columns:
1. Category
2. Accident-type (insgesamt means total for all subcategories)
3. Year
4. Month
5. Value

The application forecasts the values for:
Category: 'Alkoholunfälle'
Type: 'insgesamt

# Packages
The application uses the following packages
1. pandas
2. numpy
3. matplotlib
4. sklearn
5. pickle
6. flask

# Files
- [Training Model.ipynb](https://github.com/RidaIftikhar14/DPS-Challenge-2023-/blob/main/Model%20Training.ipynb): The notebook contains all the steps performed to create and train the AI Model.
- [app.py](https://github.com/RidaIftikhar14/DPS-Challenge-2023-/blob/main/app.py): An application which performs the forecasting and returns the result. 
- submit.py: a script to make the post to the endpoint.

# Visualization
![Trend of accidents by category](https://github.com/RidaIftikhar14/DPS-Challenge-2023-/assets/122225638/943e93cd-c92c-49ae-abea-f8e06aa4e1a1)

![Number of accidents per category](https://github.com/RidaIftikhar14/DPS-Challenge-2023-/assets/122225638/b7ef9d38-1954-4bcd-be61-aa0d3e9104be)

![Trend of accidents by category](https://github.com/RidaIftikhar14/DPS-Challenge-2023-/assets/122225638/ace7424e-f6c3-4b67-aa6b-d77ccc418169)
