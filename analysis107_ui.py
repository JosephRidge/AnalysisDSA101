#  libraries
import streamlit as st 
import pandas as pd 


#  constants 
df = pd.read_csv("data/genai_usage/genai_llm_usage_dataset_1000.csv")
rows, columns = df.shape 
output = f"Features: {columns} || Records: {rows}"


#  functions
def businessUnderstanding():
    st.markdown("# **Enterprise LLM Usage, Performance & User Satisfaction Dataset**")
    st.markdown("*Overview*")
    st.markdown("""
    - This dataset is a synthetic Generative AI (GenAI) and Large Language Model (LLM) usage dataset designed for data science, machine learning, and analytics projects.
    - It simulates real-world interactions between users and enterprise LLM applications by capturing information related to model usage, prompt characteristics, response performance, latency, token consumption, hallucinations, costs, and user satisfaction.
    *Note:This is a synthetic dataset created for educational, research, and machine learning purposes. It does not contain any real user information or proprietary data.*
    """)
    st.markdown("[Data source](https://www.kaggle.com/datasets/mirzayasirabdullah07/llm-and-generative-ai-usage-analytics-dataset)")

def dataUnderstanding():
    col1, col2  = st.columns(2)
    col1.metric("Records", rows)
    col2.metric("Features", columns) 
    st.markdown("## **Focus Areas**")
    st.markdown("""
    > - There exists 7 Focus areas (Customer support, Education, REtail, Fincance, Healthcare, Coding, Legal)
    > - Customer Support  was the most focused are with a search frequency of **165** times
    > - Education came second with 156 searches 
    > - Legal came in last with 127 searches
    """)

    st.markdown("#### **Note**")
    st.markdown("""
    - There exist no missing values
    """)

#  UI 
# Business understanding
businessUnderstanding()
st.divider()

# Data Understanding
dataUnderstanding()
st.divider()
# Data Preparation 
# Modeling
# Evaluation
# deployment ()