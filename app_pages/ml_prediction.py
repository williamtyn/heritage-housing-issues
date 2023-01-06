import streamlit as st
from src.data_management import load_pkl_file, load_houses_data, load_inherited_houses_data
import pandas as pd
from src.machine_learning.predictive_analysis import predict_sale_price

def ml_prediction_body():

    st.write("### Predict House Sale Price")

    st.info(
        f"* The client is interested the know the predictive sale price for her four inherited houses. "
        f"The client also wants to have the possibility to calculate any other house sale price in Ames, Iowa.  "
        f"Based on that, by selecting features the predictive sale price will be displayed "
    )
    st.write("---")

    # load files
    version = 'v1'
    pipeline_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/absolute_regressor_pipeline.pkl")
    house_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )
    
    st.subheader('Want to predict a house sale price?')
    st.write(
        f"Predict House Sale Price based on theese features. "
        )

    feat_meaning = [("Variable", "Meaning", "Comment"),
                    ("YearBuilt", "Original construction date	", ""),
                    ("GrLivArea", "Above ground living area square feet", ""),
                    ("TotalBsmtSF", "Total square feet of basement area", ""),
                    ("GarageArea", "Size of garage in square feet", ""),
                    ("KitchenQual", "Kitchen quality", "Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor")]

    columns = feat_meaning[0]
    data = feat_meaning[1:]
    df_meaning = pd.DataFrame(data, columns=columns).reset_index(drop=True)
    
    if st.button('See feature meaning'):
        st.dataframe(df_meaning)
    
    # Generate live data
    X_live = DrawInputsWidgets()

    sale_price_prediction_live = predict_sale_price(
        X_live, house_features, pipeline_model)

    # predict on live data
    if st.button('Predict House Sale Price'):
        price_prediction = predict_sale_price(
            X_live, house_features, pipeline_model
        )

        st.write(
            f"Predicted Sale Price for this house: **$ {sale_price_prediction_live}** "
            )

    st.write("---")

    # prediction for inherited houses
    st.subheader('Predicted Sale Price Inherited Houses')
    st.info(
        f"We have done a prediction for the four inherited houses. "
        )
    
    # load inherited houses data
    inherited_data = load_inherited_houses_data()

    house_1 = predict_sale_price(
            inherited_data.iloc[[0]], house_features, pipeline_model
        )
    house_2 = predict_sale_price(
            inherited_data.iloc[[1]], house_features, pipeline_model
        )
    house_3 = predict_sale_price(
            inherited_data.iloc[[2]], house_features, pipeline_model
        )
    house_4 = predict_sale_price(
            inherited_data.iloc[[3]], house_features, pipeline_model
        )
    
    
    st.write(
        f"Predicted House 1 Sale Price: **$ {house_1}** "
        )
    st.write(
        f"Predicted House 2 Sale Price: **$ {house_2}** "
        )
    st.write(
        f"Predicted House 3 Sale Price: **$ {house_3}** "
        )
    st.write(
        f"Predicted House 4 Sale Price: **$ {house_4}** "
        )
    

def DrawInputsWidgets():

    # load data
    df = load_houses_data()
    percentageMin, percentageMax = 0.4, 2.0

    # widgets 
    col1, col2, col3 = st.beta_columns(3)
    col4, col5, col6 = st.beta_columns(3)

    # empty dataframe
    X_live = pd.DataFrame([], index=[0])

    # Widget features: GarageArea,GrLivArea,KitchenQual,TotalBsmtSF,YearBuilt
    with col1:
        feature = 'YearBuilt'
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col2:
        feature = 'GrLivArea'
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median())
    )
    X_live[feature] = st_widget

    with col3:
        feature = 'TotalBsmtSF'
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col4:
        feature = 'GarageArea'
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget
    
    #Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor

    with col5:
        feature = "KitchenQual"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    # st.write(X_live)

    return X_live