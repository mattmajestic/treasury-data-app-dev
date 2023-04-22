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


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
#  To get rid of the Streamlit branding stuff
local_css("css/styles.css")

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
st.write("Ready to get started?")
col1, col2, col3 = st.columns(3)

with col1:
    st.button("App Insights")
    # Create some sample data
    data = {
        "year": [2010, 2011, 2012, 2013, 2014, 2015],
        "country": ["USA", "USA", "Canada", "Canada", "Mexico", "Mexico"],
        "volume": [100, 120, 90, 110, 80, 100]
    }
    df = pd.DataFrame(data)

    # Create the chart
    chart = alt.Chart(df).mark_line().encode(
        x=alt.X('year', type='nominal'),
        y=alt.Y('volume', type='quantitative'),
        color=alt.Color('country', type='nominal', scale=alt.Scale(scheme='category20')),
        tooltip=['year', 'country', 'volume']
    ).properties(
        width=600,
        height=400
    )

    # Display the chart using Streamlit
    st.altair_chart(chart, use_container_width=True)

with col2:
    st.button("API")
    st.markdown("[Treasury Data API](https://treasury-data-app-dev-backend-ypo22oeifq-uc.a.run.app/docs) to visit our API")
    st.markdown("[Treasury Data API Documentation](https://treasury-data-app-dev-backend-ypo22oeifq-uc.a.run.app/docs) to visit our API Documentation")

with col3:
    st.button("Learn More")

# Add footer
st.markdown(
    f'<p style="text-align:center;color:{secondary_color};padding-top:50px;">'
    'Made by Treasury Data App Inc.</p>',
    unsafe_allow_html=True
)
