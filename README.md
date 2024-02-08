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
- [submit.py](https://github.com/RidaIftikhar14/DPS-Challenge-2023-/blob/main/submit.py): a script to make the post to the endpoint.

# Visualization
![Number of accidents per accident type](https://github.com/RidaIftikhar14/DPS-Challenge-2023-/assets/122225638/6419c142-12bc-45d5-8e6c-a76894fbc2b0)

![Number of accidents per category](https://github.com/RidaIftikhar14/DPS-Challenge-2023-/assets/122225638/aac8de9f-c987-4125-8df0-c26d16ddb3b3)

![Trend of accidents by category](https://github.com/RidaIftikhar14/DPS-Challenge-2023-/assets/122225638/5b9cac74-426c-470b-85ef-c6909dd9a93a)

![Heroku Application](https://github.com/RidaIftikhar14/DPS-Challenge-2023-/assets/122225638/810fdfba-9ae7-4515-9122-f04e69b247d3)

