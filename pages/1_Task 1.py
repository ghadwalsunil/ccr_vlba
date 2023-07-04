import streamlit as st
import streamlit.components.v1 as components

# Initial Setup

st.set_page_config(page_title="Task 1", page_icon=":bar_chart:", layout="wide")
st.title("Task 1")
st.subheader('The average costs for a branch office must be evaluated. Consider all given data regarding rent, personnel, maintenance costs etc.')
st.markdown(
    """
<iframe width="1400" height="1050" src="https://lookerstudio.google.com/embed/reporting/e786e6f0-7e75-4a00-a6e3-edb91b1e68cf/page/p_aejxlvpm7c" frameborder="0" style="border:0" allowfullscreen></iframe>

<iframe width="1400" height="1050" src="https://lookerstudio.google.com/embed/reporting/2ba6e417-3502-47fc-974c-a4fb2dd645c3/page/tEnnC" frameborder="0" style="border:0" allowfullscreen></iframe>
""",
    unsafe_allow_html=True,
)


# def embed_data_studio_report(url):
#     report_html = f'<iframe src="{url}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>, unsafe_allow_html=True'
#     components.html(report_html, height=700)


# data_studio_url = "https://lookerstudio.google.com/reporting/65e625c8-504d-4865-94c8-e0c718b64703"
# embed_data_studio_report(data_studio_url)

