# Portfolio Project 5 - Predictive Analytics

## Predict sales price for your house in Ames, Iowa.

In this application you can calculate and predict the estimated sales price for your house in Ames, Iowa based on historical data from houses sold in the same area.

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
<li><a href="#dataset">Dataset</a></li>
<li><a href="#business-requirements">Business Requirements</a></li>
<li><a href="#business-case">Business Case Assessment</a></li>

</ul>
<li><a href="#data-understanding">Data Understanding</a></li>
<li><a href="#data-preparation">Data Preparation</a></li>
<li><a href="#modelling">Modelling</a></li>
<li><a href="#evaluation">Evaluation</a></li>
<li><a href="#deployment">Deployment</a></li>
</ul>
<li><a href="#sources">Sources</a></li>

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


<h3 id="dataset">Dataset</h3>

[House Prices Data from Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)

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

<h2 id="sources">Sources</h2>

[Text about CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/)

---

This application was completed as a Portfolio Project 5 for the Fullstack Diploma at [Code Institute](https://codeinstitute.net/se/). 

The project is for educational purposes only and not for public consumption.

William Tynér, November 2022.
[LinkedIn](https://www.linkedin.com/in/williamtyner/)