import streamlit as st
import pandas as pd
import altair as alt

# Set page configuration
st.set_page_config(
    page_title=" Treasury Data App",
    page_icon=":money_with_wings:",
    layout="wide",
    initial_sidebar_state="expanded",
    )

st.write("Supplemental Treasury Insights")
st.write("API + App for Supplemental Treasury Insights")
st.write("Welcome to our app! Our mission is to provide supplemental insights for treasury management. This app is powered by an API that pulls data from a variety of sources, and provides you with powerful tools to visualize and analyze that data.")

# Add some call-to-action buttons
st.markdown("---")
st.write("Our Products")
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.button("Insights")
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['US', 'Canada', 'Mexico'])
    st.line_chart(chart_data)

with col2:
    st.button("API")
    st.markdown("[Treasury Data API](https://treasury-data-app-dev-backend-ypo22oeifq-uc.a.run.app/docs) to visit our API")
    st.markdown("[Treasury Data API Documentation](https://treasury-data-app-dev-backend-ypo22oeifq-uc.a.run.app/docs) to visit our API Documentation")

with col3:
    st.button("Consulting")
    st.write("We provide developer & SME services to help connect you to insights")

# Add footer
st.markdown(
    'Made by Treasury Data App Inc Run on Google Cloud</p>',
    unsafe_allow_html=True
)
