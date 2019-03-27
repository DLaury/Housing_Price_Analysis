# Housing_Price_Analysis\
![Alt text](https://a1.r9cdn.net/rimg/himg/ef/91/94/sembo-US-H254064-294144a_hb_a_003.jpg_resizeMode=FitInside_formatSettings=jpeg(quality-90)-663391.jpg?width=500&height=350&crop=true&caller=HotelDetailsPhoto "Iowa House")

Our team set out to create a machine learning algorithm that can predict of sale prices of homes in Ames, Iowa by using datasets from Kaggle to analyze similar features of houses. The data sets can be found on our site and here: https://www.kaggle.com/c/house-prices-advanced-regression-techniques.

By applying a machine learning regression algorithm we were able to train our program to see the effect of different individual house features (Size, quality, etc) on the final sale price of the house. To showcase this we built a website where you can input the parameters of a new house and the algorithm will return it's predicted value.

## Overview
![Alt text](https://github.com/DLaury/Housing_Price_Analysis/blob/master/Iowa%20Images/Correlation%20Matrix.JPG)

![Alt text](https://github.com/DLaury/Housing_Price_Analysis/blob/master/Iowa%20Images/Correlation%20Matrix%202.JPG)


**Home Features Used:**
![Alt text](https://github.com/DLaury/Housing_Price_Analysis/blob/master/Iowa%20Images/Dataframe.png)

Overall house Quality
Total living area not including basement
Number of spaces available for cars in a garage
Garage Size (Square Feet)
Total Basement Square Feet
1st floor square feet

**Model:**
![Alt text](https://github.com/DLaury/Housing_Price_Analysis/blob/master/Iowa%20Images/Elastic_Net_Model.png)

Elastic Net Regression was used because it works well with datasets that have correlated paramters. (e.g. Number of cars and garage size)

Mean Squared Error (MSE): Measures the average difference between the estimated values and what is estimated. The closer the MSE is to zero the better the models is predicting values.

R-Squared(R2): Measures how close the data are to the fitted regression line/the percentage of the response variable variation that is explained by a linear model. A score of 100% indicates that the model explains all of the variability of the response data around its mean. 


**Results:**

![Alt text](https://github.com/DLaury/Housing_Price_Analysis/blob/master/Iowa%20Images/Chart.png)

![Alt text](https://github.com/DLaury/Housing_Price_Analysis/blob/master/Iowa%20Images/Predictions_Vs_Actual.png)

Our scores indicate that our model explains 79.8% of the response variable variation, and have an average error of 0.233. Put more simply, our model is able to predict what the selling price of a house in Ames, Iowa will be with an accuracy rate of about 80% 


