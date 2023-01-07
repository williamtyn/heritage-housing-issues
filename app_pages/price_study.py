from src.data_management import load_houses_data
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import ppscore as pps


def correlation_study():
    """
    display top 5 correlation with Sales Price
    """

    df = load_houses_data()
    df_scatter = df.copy()

    df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)

    vars_to_study = ['OverallQual', 'GrLivArea', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'YearBuilt']

    st.write("### House Prices Correlation Study")
    st.success(
        f"**Business Requirement 1**\n"
        f"* The client is interested in discovering how the house attributes correlate with the sale price. \n"
        f"Therefore, the client expects data visualizations of the correlated variables against the sale price to show that."
        )

    # inspect data
    if st.checkbox("Inspect House Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"below you can see the first 10 rows.")

        st.write(df.head(10))

        st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to Sale Price. \n"
        f"The most correlated variable are: \n"
        f"**{vars_to_study}**"
        )

    st.subheader('Select method to see correlated features:')

    # Checkbox for displaying correlated features
    if st.checkbox("Pearson Correlation"):
        heatmap_corr(df=df_corr_pearson, threshold=0.5,
                     figsize=(20, 12), font_annot=10)

    if st.checkbox("Spearman Correlation"):
        heatmap_corr(df=df_corr_spearman, threshold=0.5,
                     figsize=(20, 12), font_annot=10)

    if st.checkbox("Predictive Power Score"):
        heatmap_pps(df=pps_matrix, threshold=0.2,
                    figsize=(20, 12), font_annot=10)

    # Text based on "House Prices Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"**Correlation Indications**\n\n"
        f"The correlation indications and plots below interpretation converge. "
        f"It is indicated that: \n"
        f"* The house price is higher when the first floor area is bigger.\n"
        f"* The house price is higher when the above ground area is bigger.\n"
        f"* The house price is higher when the house has a garage, depending on the size of the garage.\n"
        f"* The house price is higher the better overall quality there is on the house.\n"
        f"* The house price is higher the younger the house is.\n"
        )
    
    
    # Code copied from "02 - House Prices Study" notebook - "EDA on selected variables" section
    df_eda = df_scatter.filter(vars_to_study + ['SalePrice'])

    st.subheader('Select features to see a correlation with Sale Price:')
    
    st.write(
        f"Uncheck other boxes on this page to see the plot of the correlated feature with Sale Price."
        )
    # Checkbox for scatterplot on selected feature
    if st.checkbox("OverallQual"):
        corr_overallqual(df_eda)

    if st.checkbox("1stFlrSF"):
        corr_1stflrsf(df_eda)

    if st.checkbox("GrLivArea"):
        corr_grlivarea(df_eda)

    if st.checkbox("GarageArea"):
        corr_garagearea(df_eda)
        
    if st.checkbox("TotalBsmtSF"):
        corr_totalbsmtsf(df_eda)

    if st.checkbox("YearBuilt"):
        corr_yearbuilt(df_eda)
        
    df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)

# functions to plot features correlation with Sale Price
def corr_overallqual(df_eda):
    corr = df_eda["SalePrice"].corr(df_eda["OverallQual"])

    plt.scatter(df_eda["OverallQual"], df_eda["SalePrice"])
    plt.xlabel("OverallQual")
    plt.ylabel("Sale Price ($)")
    st.pyplot(plt.gcf())

def corr_1stflrsf(df_eda):
    corr = df_eda["SalePrice"].corr(df_eda["1stFlrSF"])

    plt.scatter(df_eda["1stFlrSF"], df_eda["SalePrice"])
    plt.xlabel("1stFlrSF (sq ft)")
    plt.ylabel("Sale Price ($)")
    st.pyplot(plt.gcf())

def corr_grlivarea(df_eda):
    corr = df_eda["SalePrice"].corr(df_eda["GrLivArea"])

    plt.scatter(df_eda["GrLivArea"], df_eda["SalePrice"])
    plt.xlabel("GrLivArea (sq ft)")
    plt.ylabel("Sale Price ($)")
    st.pyplot(plt.gcf())

def corr_garagearea(df_eda):
    corr = df_eda["SalePrice"].corr(df_eda["GarageArea"])

    plt.scatter(df_eda["GarageArea"], df_eda["SalePrice"])
    plt.xlabel("GarageArea (sq ft)")
    plt.ylabel("Sale Price ($)")
    st.pyplot(plt.gcf())

def corr_totalbsmtsf(df_eda):
    corr = df_eda["SalePrice"].corr(df_eda["TotalBsmtSF"])

    plt.scatter(df_eda["TotalBsmtSF"], df_eda["SalePrice"])
    plt.xlabel("TotalBsmtSF (sq ft)")
    plt.ylabel("Sale Price ($)")
    st.pyplot(plt.gcf())

def corr_yearbuilt(df_eda):
    corr = df_eda["SalePrice"].corr(df_eda["YearBuilt"])

    plt.scatter(df_eda["YearBuilt"], df_eda["SalePrice"])
    plt.xlabel("YearBuilt")
    plt.ylabel("Sale Price ($)")
    st.pyplot(plt.gcf())


# function for correlated heatmap and pps
def heatmap_corr(df,threshold, figsize=(20,12), font_annot = 8):
  if len(df.columns) > 1:
    mask = np.zeros_like(df, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    mask[abs(df) < threshold] = True

    fig, axes = plt.subplots(figsize=figsize)
    sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                linewidth=0.5
                     )
    axes.set_yticklabels(df.columns, rotation = 0)
    plt.ylim(len(df.columns),0)
    st.pyplot(fig)


def heatmap_pps(df,threshold, figsize=(20,12), font_annot = 8):
    if len(df.columns) > 1:
      mask = np.zeros_like(df, dtype=np.bool)
      mask[abs(df) < threshold] = True

      fig, ax = plt.subplots(figsize=figsize)
      ax = sns.heatmap(df, annot=True, xticklabels=True,yticklabels=True,
                       mask=mask,cmap='rocket_r', annot_kws={"size": font_annot},
                       linewidth=0.05,linecolor='grey')
      
      plt.ylim(len(df.columns),0)
      st.pyplot(fig)

def CalculateCorrAndPPS(df):
    df_corr_spearman = df.corr(method="spearman")
    df_corr_pearson = df.corr(method="pearson")
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

    return df_corr_pearson, df_corr_spearman, pps_matrix