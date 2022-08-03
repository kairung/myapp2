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

st.header("ตัวอย่างของข้อมูล")
if st.button("แสดงข้อมูล"):
   st.write(df.head(20))

#st.table(df)
st.header("การจินตทัศน์ข้อมูล")
if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.write(df.head(20))
   st.area_chart(df)

st.title("การออกแบบสรรถนะการเรียนรู้ด้านAI 5 ด้าน")

st.radio("ด้านที่ 1",["สูง","กลาง","ต่ำ"])
st.radio("ด้านที่ 2",["สูง","กลาง","ต่ำ"])
st.radio("ด้านที่ 3",["สูง","กลาง","ต่ำ"])
st.radio("ด้านที่ 4",["สูง","กลาง","ต่ำ"])
st.radio("ด้านที่ 5",["สูง","กลาง","ต่ำ"])
st.button("ออกแบบ")