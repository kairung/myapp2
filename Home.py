from nbformat import write
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots


#st.image("./pic/01.png")

html_temp="""
<div style="background-color:#80ced6;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<h3>การวิเคราะห์และออกแบบสมรรถการเรียนรู้ด้าน AI</h3>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
st.header("----------------------------------------------------------")
st.subheader("สมรรถนะการเรียนรู้ทาง AI 5 ด้าน ประกอบด้วย")
ai5="""
    1.ด้านการรับรู้สภาวะแวดล้อม <br>
    2.การแทนความรู้และการให้เหตุผล <br>
    3.การเรียนรู้ของเครื่อง <br>
    4.การโต้ตอบอย่างเป็นธรรมชาติ <br>
    5.ผลกระทบของปัญญาประดิษฐ์ต่อสังคม <br>
"""
st.markdown(ai5,unsafe_allow_html=True)
st.balloons()
st.sidebar.markdown("# 🎉หน้าแรก🎉")

def radar_chart(val1,val2,val3,val4,val5):
    df=pd.DataFrame(dict(
        r=[val1,val2,val3,val4,val5],
        theta=["x1","x2","x3","x4","x5"]))
    fig=px.line_polar(df,r='r',theta='theta',line_close=True)
    st.write(fig)

st.subheader("เกณฑ์การให้คะแนนแต่ละระดับวัดได้ดังนี้")

st.markdown("ระดับประถมศึกษาปีที่ 1",unsafe_allow_html=True)
radar_chart(5,2,7,9,4)

from plotly import graph_objs as go
from plotly.tools import make_subplots
import plotly.plotly as py

fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"), row=1, col=1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=2)
py.plot(fig)