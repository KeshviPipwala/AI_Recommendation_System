import streamlit as st
import pandas as pd
from recommendation_system import recommend_items  # Import recommendation function

st.title("AI-Powered Recommendation System")
user_id = st.number_input("Enter User ID", min_value=1, step=1)

if st.button("Get Recommendations"):
    recommendations = recommend_items(user_id)  # Call function
    st.write("### Recommended Items:")
    st.write(recommendations)
