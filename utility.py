#  visualizations
import streamlit as st 
import matplotlib.pyplot as plt 

def plotPieChart(frequencies, labels):
    fig1, ax1 = plt.subplots()
    ax1.pie(frequencies, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)