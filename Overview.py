import streamlit as st
import streamlit.components.v1 as components

# Initial Setup

st.set_page_config(page_title="Data Exploration and Analysis", page_icon=":bar_chart:", layout="wide")
st.title("Task Overview")
st.write('Mobility Worldwide (MWW) is a global corporation with an emphasis on services, production, talent promotion, and innovation in the domain of mobility. With the motive of keeping an edge over the competitors, MWW regularly assesses new technical advancements and implements them into its present internal systems once they are considered worthwhile and beneficial. The region above which MWW operates is segregated into several strategic regions with a bunch of branch offices under it for ease of operational control.')
st.subheader('CCR Scenario:') 
st.write('The Consulting and Customer Retention(CCR) department is responsible for client consultations at all interaction levels, from large auto dealerships to representing the company at trade shows. Employees start their business trips from their allocated branch locations. Members of group 01 has been hired as analysts in the CCR department and asked by the board to utilize historical data on employees, previous business trips, maintenance costs of branches, and required business assets. The motive is to analyze the data and determine the financial viability of the current stores as well as the profitability of opening a branch in a new location within the strategic region.')


st.title("Data Exploration and Analysis")
st.markdown(
    """
<iframe width="1500" height="900" src="https://lookerstudio.google.com/embed/reporting/5bc4ef0b-c2bb-4439-adf4-d2145fec742a/page/tEnnC" frameborder="0" style="border:0" allowfullscreen></iframe>    """,
    unsafe_allow_html=True,
)


# def embed_data_studio_report(url):
#     report_html = f'<iframe src="{url}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>, unsafe_allow_html=True'
#     components.html(report_html, height=700)


# data_studio_url = "https://lookerstudio.google.com/reporting/65e625c8-504d-4865-94c8-e0c718b64703"
# embed_data_studio_report(data_studio_url)

