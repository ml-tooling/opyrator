import os

import streamlit as st

st.title("Opyrator Examples")

CUSTOM_STREAMLIT_CSS = """
div[data-testid="stBlock"] button {
  width: 100% !important;
  margin-bottom: 20px !important;
  border-color: #bfbfbf !important;
}
"""

# Add custom css settings
st.markdown(f"<style>{CUSTOM_STREAMLIT_CSS}</style>", unsafe_allow_html=True)

BADGES = """
<a href="https://gitHub.com/ml-tooling/opyrator" title="Star Repo"><img src="https://img.shields.io/github/stars/ml-tooling/opyrator.svg?logo=github&style=social"></a>
<a href="https://twitter.com/mltooling" title="Follow on Twitter"><img src="https://img.shields.io/twitter/follow/mltooling.svg?style=social&label=Follow"></a>
<a href="ttps://mltooling.substack.com/subscribe" title="Subscribe to newsletter"><img src="http://bit.ly/2Md9rxM"></a>
"""
st.markdown(BADGES, unsafe_allow_html=True)

# print(next(os.walk("."))[1])
# print([x[0] for x in os.walk(os.getcwd())])

# f = []
# for (dirpath, dirnames, filenames) in walk(os.getcwd()):
#     print(dirpath)
#     f.extend(filenames)
# print(f)

demos = [str(dir) for dir in filter(os.path.isdir, os.listdir(os.curdir))]

selected_demo = st.selectbox(
    "Select Demo",
    options=demos,
)

col1, col2 = st.beta_columns(2)
with col1:
    st.button("🌅 Launch UI")
    # st.code("opyrator launch-ui app:seperate_audio", language="plain")
with col2:
    st.button("🔌 Launch API")
    # st.code("opyrator launch-api app:seperate_audio", language="plain")

col1, col2 = st.beta_columns([1, 2])

with st.beta_expander("Code", expanded=True):
    with open(os.path.join(selected_demo, "app.py"), encoding="UTF-8") as f:
        st.code(f.read(), language="python")

with st.beta_expander("Requirements"):
    with open(os.path.join(selected_demo, "requirements.txt"), encoding="UTF-8") as f:
        st.code(f.read(), language="plain")

with st.beta_expander("Export this Opyrator"):
    col1, col2 = st.beta_columns([1, 2])
    with col1:
        st.button("📦 Export to ZIP")

    with col2:
        st.code("opyrator export app:seperate_audio my-opyrator.zip", language="plain")

    col1, col2 = st.beta_columns([1, 2])
    with col1:
        st.button("🐳 Export to Docker")

    with col2:
        st.code(
            "opyrator export app:seperate_audio --format docker my-opyrator:latest",
            language="plain",
        )
