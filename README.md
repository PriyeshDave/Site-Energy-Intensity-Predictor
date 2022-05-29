# Site Energy Intensity Prediction Application 🏢⚡
![Python](https://img.shields.io/badge/Language-python3.9-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-orange)
![Frontend](https://img.shields.io/badge/Framework-Streamlit-red)
![Deployment](https://img.shields.io/badge/Cloud-Heroku-purple)


## Introduction
According to a report issued by the International Energy Agency (IEA), the lifecycle of buildings from construction to demolition were responsible for 37% of global energy-related and process-related CO2 emissions in 2020. 
Yet it is possible to drastically reduce the energy consumption of buildings by a combination of easy-to-implement fixes and state-of-the-art strategies. 
Commercial and residential buildings are tremendous users of energy, accounting for more
than 72% of electricity use in the U.S. Among the main building performance factors (i.e., enclosure, system,
and control), that influence a building’s energy performance, building façade features are one of the major
parametric elements. The recorded Energy Use Intensity (EUI) of existing buildings performance come from
relevant organizations (such as CBECS and USGBC), which contain aggregated energy performance
information (based on the ranges of certain parameters), but it is difficult to identify the specific condition of
each building category within a selected climate zone. In addition, the averaged performance data is too
general to determine if a specific building is energy efficient or not. On the other hand, it is very timeconsuming to develop a simulation model in software to each case, which also needs very detailed
information about geometry, system, and operation schedule and control modes. This is because an
accurate energy performance prediction mainly depends on a variety of detailed data about indoor thermal
conditions, mechanical system performance, occupancy level, etc. 

## 🧭 Problem Statement: 
In this project, regression-based performance prediction model was developed to estimate **building energy consumption** based on simplified
façade attribute information and weather conditions. Building façade features, including floor_area, elevation, energy star ratings, year_built, 
year_factor, state_factor, building_class, facility_type etc., were collected over 7 years and a number of states within the United States. 
Based on this training dataset, a prediction model was established to estimate annual energy use. The developed estimation model adopted
architectural physical attributes and their dynamic ambient environmental conditions as input variables. This
prediction approach will provide a more specific baseline and goal especially in the pre-design phase, it also
could asses EUI by a minimum amount of data.

## 🧾 Description: 
This data set is collected from **The WiDS Datathon 2022** which focuses on a prediction task involving roughly **100k observations** of building energy 
usage records collected over 7 years and a number of states within the United States.

### :bar_chart: Exploratory Data Analysis:
* Exploratory Data Analysis is the first step of understanding your data and acquiring domain knowledge. 
* On using **Shapiro-Wilk** test it was found that majority of features were not following normal distribution.
* There was no outliers found using **Z-Score** estimation and **IQR**.


### :hourglass: Data Preprocessing:
* Used **KNN Imputer** to impute missing values.
* Used **LabelEncoder & TargetEncoder** of encoding categorical features in dataset.

### :mag_right: Features Selection:
* On using **Pearson's Correlation** test, it was found that many features were highly correlated. So I removed the features with collinearity.

### ⚙ Model Training:
* On training my model using several regression algorithms, the model trained with **XGBoost Regressor** gave best results. 
* Used **KFold** with 10 splits cross validation with hyper-parameter tuning on XGBoost Regressor (baseline model) using **GridSearchCV**.
* Currently the model predicts with an **Adjusted R2 score of .88 and .76** on training and validation data respectively and the **RMSE of 28.7**.
* The objective is to increase the model's performance by reducing the RMSE.

## Web Application :computer: :earth_americas: :
Built a web application using **Streamlit** and deployed on **Heroku**.
<img width="960" alt="image" src="https://user-images.githubusercontent.com/81012989/158674282-b53c7be6-01b5-44c6-9b9c-1c9bce25e927.png">
https://site-energy-intensity-predict.herokuapp.com/







