# Portfolio Project 5 - Predictive Analytics

## Predict sales price for your house in Ames, Iowa.

In this application you can calculate and predict the estimated sales price for your house in Ames, Iowa based on historical data from houses sold in the same area.

![Application Mockup](./static/media/mockup.png)

## Live Site
[Go to application]()

## Repository
[View repository](https://github.com/williamtyn/heritage-housing-issues)

---

## Catalouge
<li><a href="#crisp-dm">CRoss Industry Standard Process for Data Mining (CRISP-DM)</a></li>
<ul>
<li><a href="#business-understanding">Business Understanding</a></li>
<ul>
<li><a href="#storytelling">Storytelling</a></li>
<li><a href="#project-epics">Project Epics</a></li>
<li><a href="#dataset">Dataset</a></li>
<li><a href="#hypothesis">Hypothesis and validation</a></li>

<li><a href="#business-requirements">Business Requirements</a></li>
<li><a href="#business-case">Business Case Assessment</a></li>
<li><a href="#map-business-requirements">Mapping Business Requirements</a></li>
<li><a href="#ml-business-case">ML Business Case</a></li>
</ul>
<li><a href="#data-understanding">Data Understanding</a></li>
<ul>
<li><a href="#data-reviewing">Data reviewing</a></li>
</ul>
<li><a href="#data-preparation">Data Preparation</a></li>
<ul>
<li><a href="#data-cleaning">Data Cleaning</a></li>
<li><a href="#feature-engineering">Feature Engineering</a></li>
</ul>
<li><a href="#modelling">Modelling</a></li>
<li><a href="#evaluation">Evaluation</a></li>
<li><a href="#deployment">Deployment</a></li>
</ul>
<li><a href="#dashboard-design">Dashboard Design</a></li>
<ul>
<li><a href="#dashboard-1">Page 1: Quick Project Summary</a></li>
<li><a href="#dashboard-2">Page 2: House Sale Price Study</a></li>
<li><a href="#dashboard-3">Page 3: House Sale Price Predictor</a></li>
<li><a href="#dashboard-4">Page 4: Project Hypothesis and Validation</a></li>
<li><a href="#dashboard-5">Page 5: ML Model Performance</a></li>
</ul>
<li><a href="#libraries">Libraries</a></li>
<li><a href="#technologies">Technologies</a></li>
<li><a href="#bugs">Bugs</a></li>
<li><a href="#sources">Sources</a></li>
<li><a href="#acknowledgements">Acknowledgements</a></li>

---

<h2 id="crisp-dm">CRoss Industry Standard Process for Data Mining (CRISP-DM)</h2>
In this project the flow and structure was used with the CRoss Industry Standard Process for Data Mining called Crisp-DM.

The CRoss Industry Standard Process for Data Mining (CRISP-DM) is a process model that serves as the base for a data science process. It has six sequential phases:

* Business understanding – What does the business need?

* Data understanding – What data do we have / need? Is it clean?

* Data preparation – How do we organize the data for modeling?

* Modeling – What modeling techniques should we apply?

* Evaluation – Which model best meets the business objectives?

* Deployment – How do stakeholders access the results?

Published in 1999 to standardize data mining processes across industries, it has since become the most common methodology for data mining, analytics, and data science projects.


<h2 id="business-understanding">Business Understanding</h2>
What does the business need?


<h3 id="storytelling">Storytelling</h3>
Lydia Doe, has received an inheritance from a deceased great-grandfather. Included in the inheritance are four houses located in Ames, Iowa, USA. Although Lydia has an excellent understanding of property prices in her home country of Belgium, she fears that basing her estimates for property worth on her current knowledge of the Iowan market might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa.

Lydia needs help if she is to maximize the sales price for the inherited properties. She decides to ask a Data Practitioner for help. Her reasons for doing so are:

1. She doesn't know the worth of the properties and does not want to take the risk of inaccurate pricing estimation, since there is potentially a reasonable amount of money to be made or lost when selling the four properties.

2. She is also interested in predicting the sale price from any house in Ames, Iowa in case of future property ownership in that area.

From searching the Internet, Lydia found a public dataset with house prices for Ames, Iowa, and have provided us with that.


<h3 id="project-epics">Project Epics</h3>
The project worksflow is based on Epics and can be found [here](https://github.com/users/williamtyn/projects/4)


<h3 id="dataset">Dataset</h3>

[House Prices Data from Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)


| Variable         | Meaning                                                     | Units                                                                                |
|------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above ground (i.e. does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

**Project Terms & Jargon**
* Sale Price is the Price the house have been sold for.
* Estimated Sale Price is the Price the model estimates the house to be sold for.


<h3 id="hypothesis">Hypothesis and how to validate?</h3>

1. The first hypothesis is that houses with more **GrLivArea** has higher **SalesPrice**.
* A Correlation study can help in this investigation.

2. Another hypothesis is that the younger the house is **YearBuilt** the better the **OverallCond** is of the house.
* A Correlation study can help in this investigation.

<h3 id="business-requirements">Business Requirements</h3>

1. The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.

2. The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa.


<h3 id="business-case">Business Case Assessment</h3>

1. What are the business requirements?
* The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.

* The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.

2. Is there any business requirement that can be answered with conventional data analysis?
* Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

3. Does the client need a dashboard or an API endpoint?
* The client needs a dashboard

4. What does the client consider as a successful project outcome?
* A study showing the most relevant variables correlated to sale price.
* Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.

5. Can you break down the project into Epics and User Stories?
* Information gathering and data collection.
* Data visualization, cleaning, and preparation.
* Model training, optimization and validation.
* Dashboard planning, designing, and development.
* Dashboard deployment and release.

Project Epics can be found [here](https://github.com/users/williamtyn/projects/4).

6. Ethical or Privacy concerns?
* No. The client found a public dataset.

7. Does the data suggest a particular model?
* The data suggests a regressor where the target is the sale price.

8. What are the model's inputs and intended outputs?
* The inputs are house attribute information and the output is the predicted sale price.

9. What are the criteria for the performance goal of the predictions?
* We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.

10. How will the client benefit?
* The client will maximize the sales price for the inherited properties.

<h3 id="map-business-requirements">Map Business Requirements to Data Visualizations and ML tasks</h3>

**Business Requirement 1:** Data Visualization and Correlation
* We will inspect the data related to house prices.
* We will perform a correlation study to investigate the most relevant variables correlated to the sale price.
* We will visualize these variables against the sale price, display and summarize the insights.

**Business Requirement 2:** Regression and Data Analysis
* We will deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses.
* We will use conventional ML to map the relationships between the features and the target.
* We will use Regression as method to estimate relationship between variables and target.

<h3 id="ml-business-case">ML Business Case</h3>

#### Predict House Prices in Ames, Iowa
**Regression model**
* We want an ML model to predict House Prices in Ames, Iowa. With the model Lydia can make the right descision with the 4 houses she have inherited. The target variable is numerical and contains the estimated house price based on choosen features. We consider a regression model, which is supervised and uni-dimensional.
* Our ideal outcome is to provide Lydia with reliable insights so she feel comfortable making good descisions for her houses and possibly future houses.
* The model success metrics are:
** At least 0.7 for R2 score, on train and test set.
* The ML model is considered a failure if the model is wrong by more than 30% after 12 months, the prediction need to be consistent over a long period of time.
* The output is defined as a numerical value for price in dollars. The prediction is made on the fly (not in batches).

<h2 id="data-understanding">Data Understanding</h2>
<h3 id="data-reviewing">Data reviewing</h3>

**Missing data**

| Variable         | Meaning                                                     | Comment                                                                                |
|------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------|
|1stFlrSF|First Floor square feet||
|2ndFlrSF|Second-floor square feet|5,9% missing data|
|BedroomAbvGr|Bedrooms above ground (i.e. does NOT include basement bedrooms)|6,8% missing data|
|BsmtExposure|Refers to walkout or garden level walls||
|BsmtFinType1|Rating of basement finished area|7,8% missing data|
|BsmtFinSF1|Type 1 finished square feet||
|BsmtUnfSF|Unfinished square feet of basement area||
|TotalBsmtSF|Total square feet of basement area||
|GarageArea|Size of garage in square feet||
|GarageFinish|Interior finish of the garage|11,1% missing data|
|GarageYrBlt|Year garage was built|5,5% missing data|
|GrLivArea|Above grade (ground) living area square feet||
|KitchenQual|Kitchen quality||
|LotArea| Lot size in square feet||
|LotFrontage| Linear feet of street connected to property|17,7% missing data|
|MasVnrArea|Masonry veneer area in square feet|59% missing data|
|EnclosedPorch|Enclosed porch area in square feet|90,7% missing data|
|OpenPorchSF|Open porch area in square feet||
|OverallCond|Rates the overall condition of the house||
|OverallQual|Rates the overall material and finish of the house||
|WoodDeckSF|Wood deck area in square feet|5,3% missing data|
|YearBuilt|Original construction date||
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)||
|SalePrice|Sale Price||

**Target**

Target is good with 100% of its data filled.

**Type of features**

Totally there is 24 features:
* 4 categorical
* 20 numerical 

<h2 id="data-preparation">Data Preparation</h2>
<h3 id="data-cleaning">Data Cleaning</h3>

**Drop features**
* EnclosedPorch
Had **90,7%** of missing data. Due to that high amount of missing data, we descided to drop the feature.

**Mean value**
* BedroomAbvGr
We must asume that all houses have bedrooms above ground so the best descision is to fill the missing rows with the mean.

* GarageYrBlt 
We first asumed that if there was NaN in this data, the House didn´t have a garage. But after inspecting the data we found that some rows had information in GarageArea but not in YearBuilt, therefore we descided to use the mean method for this feature.

* LotFrontage
It is reasonable to assume that NaN means 0 (no street is connected). But the smallest value for this feature is 21 which is far from 0. Therefore we use the mean method for this feature.

**NaN to 0**
* 2ndFlrSF
We assume that NaN is not filled in because the house does not have a second floor, therefore we change the value from NaN to 0.

* MasVnrArea
We assume that NaN is not filled in because the house does not have masonry veneer walls, therefore we change the value from NaN to 0.

* WoodDeckSF
We assume that NaN is not filled in because the house does not have wooddeck, therefore we change the value from NaN to 0.

**NaN to None**
* BsmtFinType1
We assume this feature have missing values when the house don´t have a basement.

* GarageFinish
We assume this feature have missing values when the house don´t have a garage.

<h3 id="feature-engineering">Feature Engineering</h3>

#### Transformation

**Numerical**

Transformation methods that was checked:
Logarithmic in base e, Logarithmic in base 10, Reciprocal, Power, BoxCox, Yeo Johnson

* 1stFlrSF: None of the tranformation method made the distribution better.
* 2ndFlrSF: None of the tranformation method made the distribution better.
* BedroomAbvGr: None of the tranformation method made the distribution better.
* BsmtFinSF1: None of the tranformation method made the distribution better.
* BsmtUnfSF: Better distribution and handled outliers with yeo_johnson.
* TotalBsmtSF: None of the tranformation method made the distribution better.
* GarageArea: None of the tranformation method made the distribution better.
* GarageYrBlt: None of the tranformation method made the distribution better.
* GrLivArea: Better distribution with yeo_johnson.
* LotArea: None of the tranformation method made the distribution better.
* LotFrontage: None of the tranformation method made the distribution better.
* MasVnrArea: None of the tranformation method made the distribution better.
* OpenPorchSF: None of the tranformation method made the distribution better.
* OverallCond: None of the tranformation method made the distribution better.
* OverallQual: None of the tranformation method made the distribution better.
* WoodDeckSF: None of the tranformation method made the distribution better.
* YearBuilt: None of the tranformation method made the distribution better.
* YearRemodAdd: None of the tranformation method made the distribution better.

**Categorical**

* BsmtExposure: Tranformation with Ordinal Encoder from categorical to numerical
* BsmtFinType1: Tranformation with Ordinal Encoder from categorical to numerical
* GarageFinish: Tranformation with Ordinal Encoder from categorical to numerical
* KitchenQual: Tranformation with Ordinal Encoder from categorical to numerical

**SmartCorrelatedSelection**

All features was selected and after transformation done with spearman and threshold 0.6 this is the features to drop:
* 1stFlrSF
* 2ndFlrSF
* GarageArea
* GarageYrBlt
* OverallQual
* YearRemodAdd

<h2 id="modelling">Modelling</h2>

<h3 id="create-pipeline">Create ML Pipeline</h3>

We dropped the feature "EnclosedPorch" when loading the data because it had over 90% missing values.

We used the transformation methods from feature engineering section to clean and engineer the data from missing values.
* MeanMedianImputer: To replace missing values for 'BedroomAbvGr', 'GarageYrBlt', 'LotFrontage' with **mean**.
* CategoricalImputer: To replace missing values for 'GarageFinish', 'BsmtFinType1' with **None**.
* ArbitraryNumberImputer: To replace missing values for '2ndFlrSF', 'MasVnrArea', 'WoodDeckSF' with **0**.
* OrdinalCategoricalEncoder: To convert the categorical features 'BsmtExposure', 'BsmtFinType1', 'GarageFinish', 'KitchenQual' to **Numerical** to fit the model.
* SmartCorrelatedSelection: To check for strongly correlated features and drop the other features that show the same data.
* StandardScaler: To performs the task of Standardization for numerical features to have common scale when building the model.

<h3 id="split-data">Split data to Train/Test set</h3>
After creating the pipline we splitted the data to Train and Test set with 80%, 20% ratio.

<h3 id="gridsearchcv">Grid Search CV</h3>
We used hyperparameters to find the best suitable algorithm. Before this step we assumed Linear Regression would be the best possible fit to this data due to information we found on the internet. Surprising after cross validation we found out that ExtraTreesRegressor had the best mean score of 0.80.

After that we checked different parameters and got a result for both the best model and parameters which we could add to the pipeline.


<h2 id="evaluation">Evaluation</h2>
In our first attempt with this model we reached a R2 Score of **0.80**. After hyperparameter optimization we reched the R2 score of **0.93** on train set and **0.83** on test set.

* Train Set
R2 Score: 0.933
Mean Absolute Error: 14264.592
Mean Squared Error: 412323737.772
Root Mean Squared Error: 20305.756


* Test Set
R2 Score: 0.833
Mean Absolute Error: 21054.416
Mean Squared Error: 1151626233.352
Root Mean Squared Error: 33935.619

<h2 id="deployment">Deployment</h2>

<h2 id="dashboard-design">Dashboard Design</h2>
<h3 id="dashboard-1">Page 1: Quick Project Summary</h3>
A high-level summary of the project, including:

* Terms and jargon
* Information on the dataset
* The business/client requirements

<h3 id="dashboard-2">Page 2: House Sale Price Study</h3>
A page to show correlations between features and price.

* Answers Business Requirement 1
* We will inspect the data related to house prices.
* We will perform a correlation study to investigate the most relevant variables correlated to the sale price.
* We will visualize these variables against the sale price, display and summarize the insights.

<h3 id="dashboard-3">Page 3: Predict House Sale Price</h3>
On this page the client can both predict the price of her inherited houses, but also predict house sale price on any house in Ames, Iowa.

* Answers Business Requirement 2
* Widgets to predict a house sale price based on the selected features.
* Display estimated sale price on the inherite houses of the client.

<h3 id="dashboard-4">Page 4: Project Hypothesis and Validation</h3>
This page answers the hypothesis we had before we started the project.

1. The first hypothesis is that houses with more GrLivArea has higher SalesPrice.
In our House Prices Study we found out that the correlation was strong with both pearson and spearman methods, which support the hypothesis.

2. The second hypothesis is that the younger the house is YearBuilt the better the OverallCond is of the house.
After our Study we saw poor correlation between theese features, there is no evidence supporting this hypothesis.

<h3 id="dashboard-5">Page 5: ML Model Performance</h3>
This page contains information about the ml pipeline.

* Shows the ML Pipeline.
* Displays the best features the model was trained on.
* Shows Performance and evaluation.

<h2 id="libraries">Libraries</h2>

* [Numpy](https://numpy.org/doc/stable/) is used to process arrays to store values.
* [Pandas](https://pandas.pydata.org/docs/) is used to analyze data and explore data by vizalisation.
* [Matplotlib](https://matplotlib.org/) is used for creating our static plots.
* [Seaborn](https://seaborn.pydata.org/) is a library based on matplotlib and is used for statistical graphics for heatmaps in this project.
* [pandas_profiling](https://pandas-profiling.ydata.ai/docs/master/index.html) is used to import ProfileReport to better understand features by vizualisation.
* [Ppsscore](https://pypi.org/project/ppscore/) is used for identifying linear or non-linear relationships between features in the dataset.
* [Streamlit](https://docs.streamlit.io/) is the framework we used to develop the client dashboard.
* [Feature-engine](https://feature-engine.readthedocs.io/en/latest/) is used to engineer features to use in the model.
* [Imbalanced-learn](https://pypi.org/project/imbalanced-learn/) is used for imbalanced numerical data.
* [Scikit-learn](https://scikit-learn.org/stable/whats_new/v0.24.html) is used to create model pipeline and apply algoritms.

<h2 id="technologies">Technologies</h2>

* [Python](https://www.python.org/)
* [Streamlit](https://docs.streamlit.io/)
* [Github](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Heroku](https://www.heroku.com/)

<h2 id="bugs">Bugs</h2>

* **When assessing feature importances** - I got stuck when trying to assess the importance of features. I first received the error message that "None could not be passed" through ExtraTreesRegressor. Therefor i changed the transformation from None to Unf for feature **BsmtFinType1** and **GarageFinish**. When running the data cleaning pipeline, I noticed no difference in the score, which was still **0.80**, and decided to keep this transformation. I still have problem to assess feature importances and after some consultantion with Niel at CI, the problem was that i have used the wrong value for number of steps in the cleaning pipeline, after changing this i got the result.

* **Passing dataframe to predict sale price function** - I struggled a lot to load and predict the sale price for the inherited houses. I received an error message that the "load_inherited_houses_data()" function was not a pandas DataFrame and could not be used in the function, but it was saved in pandas. After a lot of reading, I tried to use the iloc attribute to access the index, and that solved the problem. So the problem was not the data itself, but rather how I tried to access it.

* **Show scatterplots for features are not showing when corr method checkbox is active** - In the dashboard study page, the scatterplots for correlated fetaures with SalePrice showing the Pearson, Spearman and PPS matrix if theese checkboxes is active. If they are not active, the scatterplots are shown as expected. Therefor i added the helptext to uncheck them to show the scatterplot.

<h2 id="sources">Sources</h2>

* [Text about CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/)
* The template for this project is provided by [Code Institute](https://codeinstitute.net/se/).
* A big part of the project workflow and functions was used from the walktrough project "Churnometer" from [Code Institute](https://codeinstitute.net/se/)

<h2 id="acknowledgements">Acknowledgements</h2>

I want to thank **Niel McEwen** for his support on Slack when i got stuck.

I want to thank **Vanessa Anna-Maria Andersson** for sharing her project and gave me some inspiration for the workflow.



---



This application was completed as a Portfolio Project 5 for the Fullstack Diploma at [Code Institute](https://codeinstitute.net/se/). 

The project is for educational purposes only and not for public consumption.

William Tynér, November 2022.
[LinkedIn](https://www.linkedin.com/in/williamtyner/)