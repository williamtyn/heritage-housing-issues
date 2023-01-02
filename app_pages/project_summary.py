import streamlit as st

def project_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**Project Terms & Jargon**\n"
        f"* **Sale Price** is the Price the house have been sold for.\n"
        f"* **Estimated Sale Price** is the Price the model estimates the house to be sold for.\n"
    )


    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/williamtyn/heritage-housing-issues/blob/main/jupyter_notebooks/Predict%20Sale%20Price.ipynb).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"**The project has 2 business requirements:**\n"
        f"* 1 - The client is interested in discovering how the house attributes correlate with the sale price. \n"
        f" Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.\n "
        
        f"* 2 - The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa. "
        )

    st.info(
        f"**Used Data**\n"
        f"* We have used a publicly available data from. \n"
        f"[Kaggle.com](https://www.kaggle.com/datasets/codeinstitute/" +
        f"housing-prices-data)"
        )