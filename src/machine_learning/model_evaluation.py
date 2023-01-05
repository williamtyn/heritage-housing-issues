import streamlit as st
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error 


# code foundation copied from "Modeling and Evaluation" notebooks
def pipeline_performance(X_train, y_train, X_test, y_test, pipeline):
    st.info("Train Set")
    confusion_matrix_and_report(X_train, y_train, pipeline)

    st.info("Test Set")
    confusion_matrix_and_report(X_test, y_test, pipeline)


def pipeline_evaluation(X,y,pipeline):
    prediction = pipeline.predict(X)
    st.write('R2 Score:', r2_score(y, prediction).round(3))
    st.write('Mean Squared Error:', mean_squared_error(y, prediction).round(3))  
    st.write('Mean Absolute Error:', mean_absolute_error(y, prediction).round(3))
