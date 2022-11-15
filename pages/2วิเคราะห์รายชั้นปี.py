import streamlit as st
import pandas as pd
import numpy as np

html_21="""
<div style="background-color:#f768a1;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
 <center><h3>การวิเคราะห์รายชั้นปี</h3></center>
</div>
"""
st.image('./pic/ban23.png')
st.markdown(html_21,unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.sidebar.markdown("# วิเคราะห์รายชั้นปี ")

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

html_22="""
<div style="background-color:#f768a1;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
<h5>รายงานสถิติของข้อมูล </h5>
</div>
"""
st.markdown(html_22,unsafe_allow_html=True)

options1 = st.multiselect(
     'กรุณาเลือกขนาดโรงเรียนต้องการวิเคราะห์',
    ['ขนาดใหญ่', 'ขนาดกลาง', 'ขนาดเล็ก', 'รวม'])
st.write('คุณเลือกดังนี้', options1)

if options1==[]:
    st.markdown("คุณยังไม่ได้เลือกระดับชั้นปีสำหรับการวิเคราะห์ข้อมูล")
else:  
    st.markdown("ใส่ข้อมูลสถิติ")
    st.markdown("ใส่ข้อมูลตัวอย่างข้อมูล")
    st.markdown("ใส่ข้อมูลการจินตทัศน์ข้อมูล")    

options2 = st.multiselect(
     'กรุณาเลือกระดับชั้นปีที่ต้องการวิเคราะห์',
    ['ป.1', 'ป.2', 'ป.3', 'ป.4', 'ป.5'])
st.write('คุณเลือกดังนี้', options2)

if options2==[]:
    st.markdown("คุณยังไม่ได้เลือกระดับชั้นปีสำหรับการวิเคราะห์ข้อมูล")
else:
    st.markdown("ใส่ข้อมูลสถิติ")
    st.markdown("ใส่ข้อมูลตัวอย่างข้อมูล")
    st.markdown("ใส่ข้อมูลการจินตทัศน์ข้อมูล")

st.subheader("การวิเคราะห์สรรถนะการเรียนรู้ด้านAI 5 ด้าน")

options3 = st.multiselect(
     'กรุณาเลือกการวิเคราะห์การเรียนรู้',
     ['ด้านที่1', 'ด้านที่2', 'ด้านที่3','ด้านที่4', 'ด้านที่5'])
st.write('คุณเลือกดังนี้', options3)
st.markdown("Radar Chart")


html_23="""
<div style="background-color:#f768a1;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
 <center><h3>การออกแบบสมรรถนะการเรียนรู้ด้าน AI </h3></center>
</div>
"""
st.markdown(html_23,unsafe_allow_html=True)
st.markdown("เลือกออกแบบการเรียนรู้ด้านที่")

options4 = st.multiselect(
     'กรุณาเลือกออกแบบ',
     ['การเรียนรู้ด้านที่1', 'การเรียนรู้ด้านที่2', 'การเรียนรู้ด้านที่3','การเรียนรู้ด้านที่4', 'การเรียนรู้ด้านที่5'])
st.write('คุณเลือกดังนี้', options4)

st.write(str(options4),"ของ",str(options2),"อยู่ในระดับที่ xxx")

if st.button("ออกแบบ"):
    if options4==[]:
        st.markdown("คุณยังไม่เลือกข้อมูลการออกแบบ กรุณาเลือกการเรียนรู้ AI ด้านที่ต้องการออกแบบก่อน")
    else:
        html_24="""
<div style="background-color:#f768d1;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>🎉คุณได้ทำการออกแบบ 🎉</h4>
        1.ด้านที่ 1 สูง <br>
        2.ด้านที่ 2 กลาง <br>
        3.ด้านที่ 3 กลาง <br>
        4.ด้านที่ 4 สูง <br>
        5.ด้านที่ 5 สูง <br>
</center>
</div>
"""
        st.markdown(html_24,unsafe_allow_html=True)
        st.button("ยังไม่ออกแบบ")   
else:
    st.write("ไม่ออกแบบ")