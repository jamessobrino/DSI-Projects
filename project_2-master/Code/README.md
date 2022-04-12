Problem Statement: Your company has been hired by local real estate agents to predict housing prices in the city of Ames, Iowa. Using machine learning, create a model that can accurately predict housing prices based on features of the houses in question.

[data description](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

|Feature|Type|Description|
|---|---|---|
|column name|int/float/object|This is an example| 
|Id|int|This column labels house with a unique id|
|Overall Qual|int|Rates the overall material and finish of the house|
|Gr Liv Area|int|Above grade (ground) living area square feet|
|Garage Area|float|Size of garage in square feet|
|Garage Cars|float|Size of garage in car capacity|
|Total Bsmt SF|float|Total square feet of basement area|
|1st Flr SF|int|First Floor square feet|
|Year Built|int|Original construction date|
|Year Remod/Add|int|Remodel date (same as construction date if no remodeling or additions)|
|Full Bath|int|Full bathrooms above grade|
|Mas Vnr Area|float|Masonry veneer area in square feet|
|TotRms AbvGrd|int|Total rooms above grade (does not include bathrooms)|
|Fireplaces|int|Number of fireplaces|
|Wood Deck SF|int|Wood deck area in square feet|
|Lot Area|int|Lot size in square feet|
|Yr Sold|int|Year Sold (YYYY)|
|SalePrice|int|Sale price $$|
|MS SubClass|object|Identifies the type of dwelling involved in the sale.|
|Lot Shape|General shape of property|
|Neighborhood|object|Physical locations within Ames city limits (map available)|
|Bldg Type|object|Type of dwelling|
|House Style|object|Style of dwelling|
|Garage Type|object|Garage location|
|Misc Feature|object|Miscellaneous feature not covered in other categories|
|Roof Style|object|Type of roof|

Summary:
The best model to use is ridge regression because many features are not independant of each other. The features with the strongest correlation values are: Overall Qual, Gr Liv Area, Total Bsmt Sf, Garage Area, Garage Cars

Recommendations: There needs to be more work on the model. More cleaning of the data is necessary. There are more features that can be added however due to constraints, only 25 columns were added. When looking at houses, identify the quality of the house, the sq ft of garage and living areas (including the basement), when it was built/remodeled, how many baths, and how many rooms. Additionally prioritize houses in Northridge Heights as they tend to be priced signficantly higher compared to other neighborhoods.
