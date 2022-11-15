import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px

html_21="""
<div style="background-color:#a1e8e4;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
 <center><h3>การวิเคราะห์รายโรงเรียน</h3></center>
</div>
"""
st.image('./pic/ban22.png')
st.markdown(html_21,unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.sidebar.markdown("# วิเคราะห์รายโรงเรียน")

def radar_chart(val1,val2,val3,val4,val5):
    df=pd.DataFrame(dict(
        r=[val1,val2,val3,val4,val5],
        theta=["ด้านที่1","ด้านที่2","ด้านที่3","ด้านที่4","ด้านที่5"]))
    fig=px.line_polar(df,r='r',theta='theta',line_close=True)
    st.write(fig)


df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

html_22="""
<div style="background-color:#bcefd0;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
<h5>รายงานสถิติของข้อมูล </h5>
</div>
"""
st.markdown(html_22,unsafe_allow_html=True)
if st.button("แสดงข้อมูลสถิติ"):
   st.write(df.describe())
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

html_23="""
<div style="background-color:#bcefd0;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
<h5>ตัวอย่างของข้อมูล </h5>
</div>
"""
st.markdown(html_23,unsafe_allow_html=True)
if st.button("แสดงข้อมูล"):
   st.write(df.head(20))
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

#st.table(df)
html_24="""
<div style="background-color:#bcefd0;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
<h5>การจินตทัศน์ข้อมูล </h5>
</div>
"""
val1=9
val2=5
val3=6
val4=7
val5=5

st.markdown(html_24,unsafe_allow_html=True)
if st.button("แสดงการจินตทัศน์ภาพรวมข้อมูลโรงเรียน"):
   radar_chart(val1,val2,val3,val4,val5)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

st.subheader("การวิเคราะห์สรรถนะการเรียนรู้ด้านAI 5 ด้าน")

options1 = st.multiselect(
     'กรุณาเลือกรายชื่อโรงเรียนที่ต้องการวิเคราะห์',
     ['รร.1', 'รร.2', 'รร.3','รร.4', 'รร.5', 'รร.6','รร.7', 'รร.8', 'รร.9','ภาพรวม'])
st.write('คุณเลือกดังนี้', options1)


if st.button("วิเคราะห์สมรรถนะ"):
    if options1==[]:
        st.markdown("คุณยังไม่เลือกข้อมูลโรงเรียนสำหรับการวิเคราะห์สมรรถนะ")
    else:
        html_25="""
<div style="background-color:#c3ecee;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>🎉คุณได้ทำการออกแบบ 🎉</h4>
        1.ด้านที่ 1 สูง <br>
        2.ด้านที่ 2 กลาง <br>
        3.ด้านที่ 3 กลาง <br>
        4.ด้านที่ 4 สูง <br>
        5.ด้านที่ 5 สูง <br>
</center>
</div>
"""
        st.markdown(html_25,unsafe_allow_html=True)
        st.markdown("show chart")
        radar_chart(val1,val2,val3,val4,val5)
        st.button("ยังไม่วิเคราะห์")    
else:
    st.write("ไม่วิเคราะห์")

html_26="""
<div style="background-color:#bcefd0;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
 <center><h3>การออกแบบสมรรถนะการเรียนรู้ด้าน AI </h3></center>
</div>
"""
st.markdown(html_26,unsafe_allow_html=True)
st.markdown("เลือกออกแบบการเรียนรู้ด้านที่")

options2 = st.multiselect(
     'กรุณาเลือกออกแบบ',
     ['การเรียนรู้ด้านที่1', 'การเรียนรู้ด้านที่2', 'การเรียนรู้ด้านที่3','การเรียนรู้ด้านที่4', 'การเรียนรู้ด้านที่5'])
st.write('คุณเลือกดังนี้', options2)

st.markdown("ด้านนี้ รร.ของคุณอยู่ในระดับที่ xxx")

if st.button("ออกแบบ"):
    if options2==[]:
        st.markdown("คุณยังไม่เลือกข้อมูลการออกแบบ กรุณาเลือกการเรียนรู้ AI ด้านที่ต้องการออกแบบก่อน")
    else:
        html_25="""
<div style="background-color:#c3ecee;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>🎉คุณได้ทำการออกแบบ 🎉</h4>
        1.ด้านที่ 1 สูง <br>
        2.ด้านที่ 2 กลาง <br>
        3.ด้านที่ 3 กลาง <br>
        4.ด้านที่ 4 สูง <br>
        5.ด้านที่ 5 สูง <br>
</center>
</div>
"""
        st.markdown(html_25,unsafe_allow_html=True)
        st.button("ยังไม่ออกแบบ")   
else:
    st.write("ไม่ออกแบบ")