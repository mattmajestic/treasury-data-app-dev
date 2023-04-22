import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Supplemental Treasury Insights",
    page_icon=":money_with_wings:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define colors
PRIMARY_COLOR = "#0072C6"  # blue
SECONDARY_COLOR = "#FFFFFF"  # white
ACCENT_COLOR = "#00A650"  # green

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

# Add some call-to-action buttons
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("")
with col2:
    if st.button("Sign Up"):
        st.write("You clicked the 'Sign Up' button!")
with col3:
    if st.button("Learn More"):
        st.write("You clicked the 'Learn More' button!")

# Add footer
st.markdown(
    f'<p style="text-align:center;color:{SECONDARY_COLOR};padding-top:50px;">'
    'Made with ❤️ by Matt & Issac</p>',
    unsafe_allow_html=True
)
