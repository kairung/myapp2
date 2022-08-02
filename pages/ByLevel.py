import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# การวิเคราะห์รายชั้นปี 🎉")
st.sidebar.markdown("# Page 2 🎉")

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)

st.bar_chart(df)