from nbformat import write
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

#st.image("./pic/01.png")

html_temp="""
<div style="background-color:blue;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:'#654FEF'">
<h3>การวิเคราะห์และออกแบบสมรรถการเรียนด้าน AI</h3>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
st.header("------------------------------------")
st.subheader("สมรรถนะการเรียนรู้ทาง AI 5 ด้าน ประกอบด้วย")
ai5="""
    1.xxxxxxxxxxxx <br>
    2.xxxxxxxxxxxx <br>
    3.xxxxxxxxxxxx <br>
    4.xxxxxxxxxxxx <br>
    5.xxxxxxxxxxxx <br>
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

radar_chart(5,2,7,9,4)