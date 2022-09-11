import streamlit as st
import pandas as pd
import numpy as np
import pickle

html_21="""
<div style="background-color: #E7CE5B ;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
 <center><h3>การวิเคราะห์รายบุคคล</h3></center>
</div>
"""
st.image('./pic/ban21.png')
st.markdown(html_21,unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.sidebar.markdown("# วิเคราะห์รายบุคคล ")

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

html_22="""
<div style="background-color: #E7CE5B ;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
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
<div style="background-color: #E7CE5B ;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
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
<div style="background-color: #E7CE5B ;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
<h5>การจินตทัศน์ข้อมูล </h5>
</div>
"""
st.markdown(html_24,unsafe_allow_html=True)
if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.write(df.head(20))
   st.bar_chart(df)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

st.subheader("การวิเคราะห์สรรถนะการเรียนรู้ด้าน AI รายบุคคล 5 ด้าน")

options1 = st.multiselect(
     'กรุณาระบุอายุ',
     ['6', '7', '8','9', '10', '11','12'])
st.write('คุณเลือกดังนี้', options1)

options2 = st.multiselect(
     'กรุณาเลือกจำนวนพี่น้อง',
     ['1คน', '2คน', '3คน','อื่นๆ'])
st.write('คุณเลือกดังนี้', options2)

options3 = st.multiselect(
     'กรุณาเลือกเป็นบุตรคนที่',
     ['คนที่1', 'คนที่2', 'คนที่3','อื่นๆ'])
st.write('คุณเลือกดังนี้', options3)

options4 = st.multiselect(
     'กรุณาเลือกสถานะบิดามารดา',
     ['1.อยู่ด้วยกัน', '2.หย่าร้าง', '3.บิดาเสีย','4.มารดาเสีย','5.อื่นๆ'])
st.write('คุณเลือกดังนี้', options4)

options5 = st.multiselect(
     'กรุณาเลือกระดับการศึกษาบิดา',
     ['1.ต่ำกว่าป.6', '2.ป.6', '3.ม.3','4.ม.6', '5.ปริญญาตรี', '6.สูงกว่าปริญญาตรี'])
st.write('คุณเลือกดังนี้', options5)

options6 = st.multiselect(
     'กรุณาเลือกระดับการศึกษามารดา',
     ['1.ต่ำกว่าป.6', '2.ป.6', '3.ม.3','4.ม.6', '5.ปริญญาตรี', '6.สูงกว่าปริญญาตรี'])
st.write('คุณเลือกดังนี้', options6)

options7 = st.multiselect(
     'กรุณาเลือกนักเรียนอาศัยอยู่กับ',
     ['1.พ่อแม่', '2.พ่อ', '3.แม่','4.ญาติ', '5.ผู้ปกครอง', '6.อื่นๆ'])
st.write('คุณเลือกดังนี้', options7)

options8 = st.multiselect(
     'กรุณาเลือกรายได้ครอบครัว',
     ['1.ต่ำกว่า 10000', '2.10001-15000', '3.15001-30000','4.30001-50000', '5.มากกว่า 50000'])
st.write('คุณเลือกดังนี้', options8)

html_25="""
<div style="background-color:coral;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>🎉ผลการทำนายรายด้าน 🎉</h4>      
</center></div>
"""
st.markdown(html_25,unsafe_allow_html=True)
#st.write(f'{options1} xxx{options2} xxx{options3}')
#if st.button("ทำนายสมรรถนะการเรียนรู้ AI รายด้าน"): 
if options1 !=[] or options2!=[] or options3 !=[] or options4 !=[] or options5 !=[]or options6 !=[] or options7 !=[]or options8 !=[] :
    
    #------- Ai ด้านที่ 1
    loaded_model = pickle.load(open('./data/model/trained_model.sav', 'rb'))
    input_data =  (7,	1,	2,	1,	2,	2,	3,	1	)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    st.write(prediction)
    if(prediction[0]==1):
        st.write("ผลการทำนายด้านที่ 1 ระดับไม่ผ่าน")
    elif (prediction[0]==2):
        st.write("ผลการทำนายด้านที่ 1 ระดับผ่าน")
    else:
        st.write("ผลการทำนายด้านที่ 1 ระดับดีมาก")
    
    #------- Ai ด้านที่ 2
    loaded_model = pickle.load(open('./data/model/trained_model.sav', 'rb'))
    input_data =  (7,	1,	2,	1,	2,	2,	3,	1	)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    st.write(prediction)
    if(prediction[0]==1):
        st.write("ผลการทำนายด้านที่ 2 ระดับไม่ผ่าน")
    elif (prediction[0]==2):
        st.write("ผลการทำนายด้านที่ 2 ระดับผ่าน")
    else:
        st.write("ผลการทำนายด้านที่ 2 ระดับดีมาก")

    #------- Ai ด้านที่ 3
    loaded_model = pickle.load(open('./data/model/trained_model.sav', 'rb'))
    input_data =  (7,	1,	2,	1,	2,	2,	3,	1	)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    st.write(prediction)
    if(prediction[0]==1):
        st.write("ผลการทำนายด้านที่ 3 ระดับไม่ผ่าน")
    elif (prediction[0]==2):
        st.write("ผลการทำนายด้านที่ 3 ระดับผ่าน")
    else:
        st.write("ผลการทำนายด้านที่ 3 ระดับดีมาก")
    #------- Ai ด้านที่ 4
    loaded_model = pickle.load(open('./data/model/trained_model.sav', 'rb'))
    input_data =  (7,	1,	2,	1,	2,	2,	3,	1	)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    st.write(prediction)
    if(prediction[0]==1):
        st.write("ผลการทำนายด้านที่ 4 ระดับไม่ผ่าน")
    elif (prediction[0]==2):
        st.write("ผลการทำนายด้านที่ 4 ระดับผ่าน")
    else:
        st.write("ผลการทำนายด้านที่ 4 ระดับดีมาก")
    
    #------- Ai ด้านที่ 5
    loaded_model = pickle.load(open('./data/model/trained_model.sav', 'rb'))
    input_data =  (7,	1,	2,	1,	2,	2,	3,	1	)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    st.write(prediction)
    if(prediction[0]==1):
        st.write("ผลการทำนายด้านที่ 5 ระดับไม่ผ่าน")
    elif (prediction[0]==2):
        st.write("ผลการทำนายด้านที่ 5 ระดับผ่าน")
    else:
        st.write("ผลการทำนายด้านที่ 5 ระดับดีมาก")

else: 
    st.write("กรุณากรอกข้อมูลการวิเคราะห์สรรถนะการเรียนรู้ด้าน AI รายบุคคล 5 ด้าน ให้ครบ<br>จึงจะทำนายได้")
