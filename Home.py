import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.markdown("#การวิเคราะห์และออกแบบสมรรถการเรียนด้าน AI")
st.markdown("# Ailca System 🎈🎈")
st.balloons()
st.sidebar.markdown("# 🎉หน้าแรก🎉")

data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
)
fig.show()