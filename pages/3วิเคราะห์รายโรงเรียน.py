import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

html_21="""
<div style="background-color:#5EAD54;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
 <center><h3>การวิเคราะห์รายโรงเรียน</h3></center>
</div>
"""
st.image('./pic/ban22.png')
st.markdown(html_21,unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.sidebar.markdown("# วิเคราะห์รายโรงเรียน")

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

html_22="""
<div style="background-color:#5EAD54;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
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
<div style="background-color:#5EAD54;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
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
<div style="background-color:#5EAD54;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
<h5>การจินตทัศน์ข้อมูล </h5>
</div>
"""
df = pd.DataFrame(
   np.random.randn(100, 3),
   columns=['x','y','z']
   )
c = alt.Chart(df).mark_circle().encode(
   x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])

st.markdown(html_24,unsafe_allow_html=True)
if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.write(df.head(20))
   st.altair_chart(c, use_container_width=True)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

st.subheader("การวิเคราะห์สรรถนะการเรียนรู้ด้านAI 5 ด้าน")

options1 = st.multiselect(
     'กรุณาเลือกรายชื่อโรงเรียนที่ต้องการวิเคราะห์',
     ['รร.1', 'รร.2', 'รร.3','รร.4', 'รร.5', 'รร.6','รร.7', 'รร.8', 'รร.9','ภาพรวม'])
st.write('คุณเลือกดังนี้', options1)

if st.button("วิเคราะห์สมรรถนะ"):
    html_25="""
<div style="background-color:coral;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
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
    st.button("ยังไม่วิเคราะห์")
    st.image('./pic/04.png')
else:
    st.write("ไม่วิเคราะห์")




html_26="""
<div style="background-color:#5EAD54;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
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
    html_25="""
<div style="background-color:coral;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
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
    st.image('./pic/04.png')
else:
    st.write("ไม่ออกแบบ")