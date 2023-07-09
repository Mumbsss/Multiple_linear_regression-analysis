## multiple-regression-model# Multiple_linear_regression-analysis
## BUSINESS PROBLEM
Homes universal is a real estate agency that helps buyers get houses and sellers get the right prices for their houses. As a data scientist I have been tasked with coming up withcoming up with insights that will enable the firm come up with the best prices based on different aspects or characteristics of the houses available and at the same time explain to the buyers the reason for the pricing of certain houses.In order to come up with clear insights that will have impact ,I will apply my analysis based on polynomial regression and Multiple regression modeling.I came up with the following questions to help guide me during my analysis.The aim of this project is to develop a multiple regression model than can predict a house's price
1. How do various factors such as the nuber of bedrooms, bathrooms, floors, and overall condition of the house impact the prices of the houses?
2.  Does the square footage (sqft_living) hav a significant impact on the prices of the houses?
   ## DATA UNDERSTANDING
    The King County Housing Data Set contains information about the size, location, condition, and other features of houses in King County. A full description of the dataset's columns can be found below.
    1.Column Names and descriptions for King County Data Set

2.id - unique identified for a house

3.dateDate - house was sold

4.pricePrice - is prediction target

5.bedroomsNumber - of Bedrooms/House

6.bathroomsNumber - of bathrooms/bedrooms

7.sqft_livingsquare - footage of the home

8.sqft_lotsquare - footage of the lot

9.floorsTotal - floors (levels) in house

10.waterfront - House which has a view to a waterfront

11.view - Has been viewed

12.condition - How good the condition is ( Overall )

13.grade - overall grade given to the housing unit, based on King County grading system

14.sqft_above - square footage of house apart from basement

15.sqft_basement - square footage of the basement

16.yr_built - Built Year

17.yr_renovated - Year when house was renovated

18.zipcode - zip

19.lat - Latitude coordinate

20.long - Longitude coordinate

21.sqft_living15 - The square footage of interior housing living space for the nearest 15 neighbors

22.sqft_lot15 - The square footage of the land lots of the nearest 15 neighbors
# Interpretation of The Model
1. How do various factors such as the number of bedrooms, bathrooms, floors, and overall condition of the house impact the prices of the houses?
From our multiple linear regression model, the coefficient estimates provide insights into the relationship between the independent variable and the target variable. So a positive coefficient for the factors above reflects on the prices in that it is higher for houses with higher positive coefficients in these factors from the model.
2. Does the square footage (sqft_living) have a significant impact on the prices of the houses?

The coefficient estimate for the 'sqft_living' variable in the multiple linear regression model indicates the change in the price associated with a one-unit increase in square footage, assuming all other variables remain constant. A positive coefficient suggests that an increase in square footage is associated with higher house prices, while a negative coefficient would indicate the opposite. 
# Conclusion
We can therefore see that there are certain features and factors that influence the price of particular houses such as the overall condition of the house and the number of rooms(bedrooms, bathrooms, living areas etc) and the sqft_living spaces. Houses that are in good condition overall, and have a lot of rooms ultimately go for higher prices and the opposite is also true. Houses that have a large sqft_living also go for higher prices as most people tend to appreciate the size and space that these houses contain.
# Recommendations
1. Home Universal should invest in maintaining the overall conditions of the houses they are trying to sell

2. The sellers should invest in particularly advertising houses that contain more rooms as those go for higher prices.

3. The sellers should also focus on houses with a particularly large living space
 as those also go for higher prices.

