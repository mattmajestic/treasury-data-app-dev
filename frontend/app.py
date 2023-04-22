import streamlit as st

# Set page configuration
st.set_page_config(
    page_title=" Treasury Data App",
    page_icon=":money_with_wings:",
    layout="wide",
    initial_sidebar_state="expanded",
    )

# Define colors
primary_color = "#0072C6" # blue
secondary_color = "#FFFFFF" # white
accent_color = "#00A650" # green

# Define page content
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-color: {primary_color};
        color: {secondary_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
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
st.write("Ready to get started?")
col1, col2, col3 = st.columns(3)

with col2:
    st.button("API")
    st.markdown("[Treasury Data API](https://treasury-data-app-dev-backend-ypo22oeifq-uc.a.run.app/docs) to visit our API")
    st.markdown("[Treasury Data API Documentation](https://treasury-data-app-dev-backend-ypo22oeifq-uc.a.run.app/docs) to visit our API Documentation")

with col3:
    st.button("Learn More")

# Add footer
st.markdown(
    f'<p style="text-align:center;color:{secondary_color};padding-top:50px;">'
    'Made with ❤️ by Matt & Issac</p>',
    unsafe_allow_html=True
)
