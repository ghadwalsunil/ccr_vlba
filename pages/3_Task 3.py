import streamlit as st
import streamlit.components.v1 as components
# Initial Setup
st.set_page_config(page_title="Task 3", page_icon=":bar_chart:", layout="wide")
st.title("Task 3")
st.subheader('Investigate whether it would be sensible to open a new branch office. Use your findings from the previous tasks and try to suggest the board where a new branch could be located. You can also reason about what effect it would have had if a new branch would have been opened at the suggested location one year ago.')
from PIL import Image

image = Image.open('images/static map.jpg')

st.image(image, caption='Map showing the density of business locations around Garbsen')

st.markdown(
    """

<iframe width="1500" height="1000" src="https://lookerstudio.google.com/embed/reporting/eaf750a5-7b7a-43e9-a9d3-fb7bad0f0c85/page/tEnnC" frameborder="0" style="border:0" allowfullscreen></iframe>""",
    unsafe_allow_html=True,
)


# def embed_data_studio_report(url):
#     report_html = f'<iframe src="{url}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>, unsafe_allow_html=True'
#     components.html(report_html, height=700)
# <iframe width="1500" height="1000" src="https://lookerstudio.google.com/embed/reporting/2ba6e417-3502-47fc-974c-a4fb2dd645c3/page/tEnnC" frameborder="0" style="border:0" allowfullscreen></iframe>    


# data_studio_url = "https://lookerstudio.google.com/reporting/65e625c8-504d-4865-94c8-e0c718b64703"
# embed_data_studio_report(data_studio_url)

