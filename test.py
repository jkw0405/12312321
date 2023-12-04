import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()

x = ()
y = ()

for i in range(-20, 21, 1):
    x.append(i)
    y.append(3*i*i - 5*i + 2)

plt.plot(x, y, 'rs+', linewidth = 2)
st.pyplot(fig)

import sys
sys.exit()















col = st.columns(3)
with col(0):
    a = st.number_input('insert a', step = 1)
with col(1):
    b = st.number_input('insert b', step = 1)
with col(2):
    c = st.number_input('insert c', step = 1)

y = ()
for i in x:
    y.append(a^i**2 + b*i + c)

plt.plot(x,y)

st.pyplot(fig)