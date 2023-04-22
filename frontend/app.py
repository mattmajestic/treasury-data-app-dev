import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Supplemental Treasury Insights",
    page_icon=":money_with_wings:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define colors
primary_color = "#0072C6" # blue
secondary_color = "#FFFFFF" # white
accent_color = "#00A650" # green

# Define page content
st.title("Supplemental Treasury Insights")
st.markdown("### API + App for Supplemental Treasury Insights")

st.write(
    """
    Welcome to our app! Our mission is to provide supplemental insights for treasury management. 
    This app is powered by an API that pulls data from a variety of sources, 
    and provides you with powerful tools to visualize and analyze that data.
    """
)

# Show app icon
st.image("app_icon.png")

# Add some call-to-action buttons
st.markdown("---")
st.write("Ready to get started?")
col1, col2, col3 = st.columns(3)

with col2:
    st.button("Sign Up")

with col3:
    st.button("Learn More")

# Add footer
st.markdown(
    f'<p style="text-align:center;color:{secondary_color};padding-top:50px;">'
    'Made with ❤️ by Matt & Issac</p>',
    unsafe_allow_html=True
)
