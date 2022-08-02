import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.markdown("# การวิเคราะห์รายโรงเรียน❄️")
st.sidebar.markdown("# 🎈🎈Page 4 ❄️")

df = pd.DataFrame(
   np.random.randn(500, 3),
   columns=['x','y','z']
   )

st.table(df)

c = alt.Chart(df).mark_circle().encode(
   x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])

st.altair_chart(c, use_container_width=True)