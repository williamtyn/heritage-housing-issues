import streamlit as st

def hypothesis_validation_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"After inspecting the data and before doing the study we stated the following hypothesis.\n"
        f"After doing the correlation study, we found our answer, which is described below.\n"
    )

    st.success(
        f"**Hypothesis 1**\n"
        f"* Houses with more GrLivArea should have higher SalesPrice.\n\n"
        f"The correlation study at House Prices Study supports that. \n"

    )
    st.success(
        f"**Hypothesis 2**\n"
        f"* The younger the house is YearBuilt the better the OverallCond is of the house.  \n\n"
        f"The correlation feature study did not support that hypothesis since the correlation was poor.\n"
        f"The correlation between the quality and yearbuilt was higher but not strong.\n"
    )