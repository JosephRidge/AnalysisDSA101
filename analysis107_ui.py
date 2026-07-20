# ==========================
# Enterprise LLM Analytics Dashboard
# Premium Black & Gold Theme
# ==========================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import utility as util
# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Enterprise LLM Analytics",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Read Data
df = pd.read_csv("data/genai_usage/genai_llm_usage_dataset_1000.csv")

# ---------------------------------------------------
# Custom Theme (Black & Gold)
# ---------------------------------------------------
st.markdown("""
<style>

/* ==========================
Main App
========================== */
.stApp{
    background-color:#0E0E0E;
}

/* Remove top padding */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1400px;
}

/* ==========================
Typography
========================== */

h1{
    color:#D4AF37;
    font-size:44px;
    font-weight:800;
}

h2{
    color:#D4AF37;
    font-size:28px;
    font-weight:700;
    margin-top:25px;
}

h3{
    color:#E5C45B;
}

p, li{
    color:#D8D8D8;
    font-size:16px;
}

/* ==========================
Metric Cards
========================== */

[data-testid="metric-container"]{

    background:#181818;

    border:1px solid #2B2B2B;

    padding:20px;

    border-radius:14px;

    box-shadow:0px 6px 18px rgba(0,0,0,.45);

}

[data-testid="metric-container"] label{

    color:#D4AF37;

    font-size:15px;

}

[data-testid="metric-container"] div{

    color:white;

}

/* ==========================
Containers
========================== */

[data-testid="stVerticalBlockBorderWrapper"]{

    border-radius:16px;

}

/* ==========================
Info Cards
========================== */

.card{

    background:#171717;

    border-left:6px solid #D4AF37;

    padding:20px;

    border-radius:12px;

    margin-bottom:15px;

}

/* ==========================
Divider
========================== */

hr{

    border:1px solid #2A2A2A;

}

/* ==========================
Buttons
========================== */

.stButton>button{

    background:#D4AF37;

    color:black;

    border:none;

    border-radius:8px;

    padding:10px 22px;

    font-weight:bold;

}

.stButton>button:hover{

    background:#F2D37C;

}

/* ==========================
Links
========================== */

a{

    color:#D4AF37;

    text-decoration:none;

}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------
df = pd.read_csv("data/genai_usage/genai_llm_usage_dataset_1000.csv")

rows, columns = df.shape

# ---------------------------------------------------
# HERO
# ---------------------------------------------------

st.markdown("""
<h1>
Enterprise LLM Usage Analytics
</h1>

<p style="font-size:18px;color:#B8B8B8;margin-top:-10px;">
Performance • Cost • Latency • User Satisfaction
</p>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# Executive Summary
# ---------------------------------------------------

st.subheader("Executive Summary")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Records", f"{rows:,}")
c2.metric("Features", columns)
c3.metric("Missing Values", "0")
c4.metric("Dataset Quality", "100%")

st.divider()
 

# ---------------------------------------------------
# Business Understanding
# ---------------------------------------------------

st.subheader("Business Understanding")

st.markdown("""
<div class="card">

<h3>Overview</h3>

This synthetic enterprise dataset models real-world interactions
between users and Large Language Models (LLMs). It captures
operational, performance, and user experience metrics including:

<ul>

<li>Prompt characteristics</li>

<li>Response latency</li>

<li>Token consumption</li>

<li>Operational cost</li>

<li>Hallucination occurrence</li>

<li>User satisfaction</li>

</ul>

The dataset is intended for analytics, machine learning,
dashboarding, and business intelligence projects.

</div>
""", unsafe_allow_html=True)

st.link_button(
    "Dataset Source",
    "https://www.kaggle.com/datasets/mirzayasirabdullah07/llm-and-generative-ai-usage-analytics-dataset"
)

st.divider()

# ---------------------------------------------------
# Data Understanding
# ---------------------------------------------------

st.subheader("Data Understanding")


st.markdown("""
<div>
    <h5>Where was the GenAI applied?</h5>
</div>

""", unsafe_allow_html=True)


application_domain = df['application_domain'].value_counts()
st.dataframe(application_domain)
application_domain.plot.pie(autopct='%1.1f%%')
# plt.ylabel('Count') # Hide y-label
 
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = df['application_domain'].value_counts().index 
counts =df['application_domain'].value_counts().values
 
# fig1, ax1 = plt.subplots()
# ax1.pie(counts,   labels=labels, autopct='%1.1f%%',
#         )
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.pyplot(fig1)

util.plotPieChart(frequencies=counts, labels=labels)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Focus Areas",7)
c2.metric("Top Domain","Customer Support")
c3.metric("Frequency",165)
c4.metric("Missing Values",0)

st.markdown("""

<div class="card">

<h3>Focus Area Distribution</h3>

The dataset spans seven enterprise application domains.

• Customer Support (165)

• Education (156)

• Retail

• Finance

• Healthcare

• Coding

• Legal (127)

Customer Support represents the highest observed activity,
while Legal records the lowest frequency.

</div>

""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# Prompt Length Analysis
# ---------------------------------------------------

st.subheader("Prompt Length Analysis")

st.caption(
    "Statistical summary of prompt lengths submitted to enterprise language models."
)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Average Length","1,022")
c2.metric("Std. Deviation","574")
c3.metric("Minimum","12")
c4.metric("Maximum","2,000")

st.write("")

c1,c2,c3 = st.columns(3)

c1.metric("25th Percentile","520")
c2.metric("Median","1,056")
c3.metric("75th Percentile","1,493")

st.divider()

# ---------------------------------------------------
# Future Analytics
# ---------------------------------------------------

st.subheader("Planned Analytical Modules")

left,right = st.columns(2)

with left:

    st.markdown("""
    <div class="card">

    <h3>Descriptive Analytics</h3>

    <ul>

    <li>Prompt Distribution</li>

    <li>Token Consumption</li>

    <li>Latency Analysis</li>

    <li>Cost Analysis</li>

    <li>Hallucination Trends</li>

    </ul>

    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="card">

    <h3>Advanced Analytics</h3>

    <ul>

    <li>User Satisfaction Modelling</li>

    <li>Correlation Analysis</li>

    <li>Regression Models</li>

    <li>Classification Models</li>

    <li>Business Recommendations</li>

    </ul>

    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.caption(
    "Focus Data: Enterprise LLM Usage Analytics Dashboard | Methodology: CRISP-DM | Tool: Streamlit"
)