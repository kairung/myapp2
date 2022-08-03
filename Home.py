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
    1.การรับรู้สภาวะแวดล้อม <br>
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
        theta=["ด้านที่1","ด้านที่2","ด้านที่3","ด้านที่4","ด้านที่5"]))
    fig=px.line_polar(df,r='r',theta='theta',line_close=True)
    st.write(fig)

st.subheader("เกณฑ์การให้คะแนนแต่ละระดับวัดได้ดังนี้")

st.markdown("ระดับประถมศึกษา",unsafe_allow_html=True)
dt1=np.array([6,6,3,3,9,27])
df1 = pd.DataFrame(dt1,columns=('ด้านที่1','ด้านที่2','ด้านที่3','ด้านที่4','ด้านที่5','คะแนนรวม'))
st.dataframe(df1) 

radar_chart(6,6,3,3,9)


