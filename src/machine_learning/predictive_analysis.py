import streamlit as st


def predict_sale_price(X_live, house_features, pipeline_model):
    
    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(house_features)

    # prediction
    house_price = pipeline_model.predict(X_live_sale_price)
    price_prediction = int(house_price)

    return price_prediction
