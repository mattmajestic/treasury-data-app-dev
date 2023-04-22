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

st.write(
    """
    <div style='background-color: white; padding: 25px 25px 25px 25px; border-radius: 5px;'>
    <h1 style='text-align: center; color: {primary_color};'>Supplemental Treasury Insights</h1>
    <h3 style='text-align: center; color: {accent_color};'>API + App for Supplemental Treasury Insights</h3>
    <p>Welcome to our app! Our mission is to provide supplemental insights for treasury management. This app is powered by an API that pulls data from a variety of sources, and provides you with powerful tools to visualize and analyze that data.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Add some call-to-action buttons
st.markdown("---")
st.write("Our Products")
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.button("Insights")
    # Sample data
    data = pd.DataFrame({
        'year': [2018, 2018, 2019, 2019, 2020, 2020],
        'country': ['USA', 'Canada', 'USA', 'Canada', 'USA', 'Canada'],
        'volume': [100, 200, 150, 250, 175, 225]
    })

    # Create grouped bar chart with Altair
    chart = alt.Chart(data).mark_bar().encode(
        x='year',
        y='volume',
        color='country'
    ).properties(
        width=600,
        height=400
    )

    # Display chart in Streamlit
    st.altair_chart(chart, use_container_width=True)

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
