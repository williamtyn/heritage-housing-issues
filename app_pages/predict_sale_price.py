import streamlit as st
import matplotlib.pyplot as plt
from src.data_management import load_houses_data, load_inherited_houses_data, load_pkl_file
import pandas as pd
from src.machine_learning.model_evaluation import pipeline_performance, pipeline_evaluation


def predict_sale_price_body():
    st.write("### House Sale Price Predictor")
    st.success(
            f"**Business Requirement 2**\n"
            f"* The client is interested in predicting the sale price of her four inherited houses and any other house in Ames, Iowa. \n"
            )

    # load pipeline files
    version = 'v1'
    predict_price_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/absolute_regressor_pipeline.pkl")
    feat_importance_img = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv")

    st.info(
        f"* As our Business Case tells us, the model success metrics are at least **0.7** on the train and test set.\n"
        f"* We started to use classification regressors but found out pretty soon that the performance was very low.\n"
        f"* There were most numerical features and therefore we switched to Regressor instead of Classifier and converted features so all were numerical.\n"
        f"* Our first evaluation gave a score of **0.81** on the test set and after som hyperparameter optimization we landed on **0.83** R2 Score.\n"
        )

    st.write("---")

    # show pipeline steps
    st.subheader('ML Pipeline')
    st.write("* ML pipeline to predict house sale price for any house in Ames, Iowa.")
    st.write(predict_price_pipeline)
    st.write("---")

    # show best features
    st.subheader('Best Features')
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(feat_importance_img)
    st.write("---")

    # performance and evaluation
    st.subheader('Performance and Evaluation')
    st.write("* R2 Score, Mean Absolute and Squared Error")
    pipeline_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=predict_price_pipeline,
                    )
    