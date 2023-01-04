import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.project_summary import project_summary_body
from app_pages.price_study import correlation_study
from app_pages.hypothesis_validation import hypothesis_validation_body

app = MultiPage(app_name= "Heritage Housing Issues") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", project_summary_body)
app.add_page("House Prices Correlation Study", correlation_study)
app.add_page("Hypothesis and Validation", hypothesis_validation_body)

app.run()