import streamlit as st
import streamlit.components.v1 as components

# Initial Setup
st.set_page_config(page_title="Home Page", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Overview")
st.markdown("___")


st.subheader("Intial Graph")
st.markdown(
    """
    <iframe width="1000" height="750" src="https://lookerstudio.google.com/embed/reporting/65e625c8-504d-4865-94c8-e0c718b64703/page/tEnnC" frameborder="0" style="border:0" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True,
)