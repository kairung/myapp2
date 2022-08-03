import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# 🎉การวิเคราะห์รายชั้นปี 🎉")
st.sidebar.markdown("# วิเคราะห์รายชั้นปี 🎉")

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.header("รายงานสถิติของข้อมูล")
if st.button("แสดงข้อมูลสถิติ"):
   st.write(df.describe())
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

st.header("ตัวอย่างของข้อมูล")
if st.button("แสดงข้อมูล"):
   st.write(df.head(20))
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

#st.table(df)
st.header("การจินตทัศน์ข้อมูล")
if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.write(df.head(20))
   st.area_chart(df)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

st.title("การออกแบบสรรถนะการเรียนรู้ด้านAI 5 ด้าน")

options1 = st.multiselect(
     'กรุณาเลือกออกแบบการเรียนรู้ด้านที่1',
     ['Green', 'Yellow', 'Red', 'Blue'])
st.write('คุณเลือกดังนี้', options1)

options2 = st.multiselect(
     'กรุณาเลือกออกแบบการเรียนรู้ด้านที่2',
     ['Green', 'Yellow', 'Red', 'Blue'])
st.write('คุณเลือกดังนี้', options2)

options3 = st.multiselect(
     'กรุณาเลือกออกแบบการเรียนรู้ด้านที่3',
     ['Green', 'Yellow', 'Red', 'Blue'])
st.write('คุณเลือกดังนี้', options3)

options4 = st.multiselect(
     'กรุณาเลือกออกแบบการเรียนรู้ด้านที่4',
     ['Green', 'Yellow', 'Red', 'Blue'])
st.write('คุณเลือกดังนี้', options4)

options5 = st.multiselect(
     'กรุณาเลือกออกแบบการเรียนรู้ด้านที่5',
     ['Green', 'Yellow', 'Red', 'Blue'])
st.write('คุณเลือกดังนี้', options5)



st.button("ออกแบบ")