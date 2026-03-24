
# In[1]:
import streamlit as st

st.set_page_config(
    page_title="PolyFlood360",
    page_icon="💧",
    layout="wide"
)

st.title("💧 PolyFlood360 – Polymer Flood Surveillance Platform")
st.markdown("""
Welcome to **PolyFlood360**, your integrated surveillance, optimization, 
diagnostics, and machine learning dashboard for polymer floods.

Use the sidebar to navigate through modules.
""")

st.header("📊 Key Field KPIs (Example Placeholder)")

import plotly.express as px
import pandas as pd
import numpy as np

# Fake demo dataset
days = np.arange(1, 31)
oil = np.random.normal(1200, 50, 30)
water = np.random.normal(8000, 400, 30)
polymer = np.random.normal(1500, 100, 30)

df = pd.DataFrame({"Day": days, "Oil": oil, "Water": water, "Polymer": polymer})

fig = px.line(df, x="Day", y=["Oil", "Water", "Polymer"],
              title="Daily Oil, Water & Polymer Injection")
st.plotly_chart(fig, use_container_width=True)

# In[2]:
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Field Surveillance Dashboard")

st.markdown("""
This page shows high‑level field KPIs including VRR, watercut, injection pressure 
compliance, and polymer usage.
""")

uploaded_file = st.file_uploader("Upload Field Data (CSV/Excel)", type=["csv", "xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    st.subheader("✅ Data Preview")
    st.dataframe(df.head())

    if all(col in df.columns for col in ["Date", "Oil", "Water", "Injection"]):
        fig = px.line(df, x="Date", y=["Oil", "Water", "Injection"], title="Field Production & Injection")
        st.plotly_chart(fig, use_container_width=True)

# In[3]:
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💧 Injector Surveillance")

st.markdown("""
Upload injector data with columns like:
- Date  
- Well  
- Rate  
- WHP  
- BHP  
- Polymer_Conc  
""")

inj_file = st.file_uploader("Upload Injector Data", type=["csv", "xlsx"])

if inj_file:
    df = pd.read_csv(inj_file) if inj_file.name.endswith(".csv") else pd.read_excel(inj_file)
    st.dataframe(df.head())

    wells = df["Well"].unique()
    selected = st.selectbox("Select Injector", wells)

    wdf = df[df["Well"] == selected]

    fig = px.line(wdf, x="Date", y="Rate", title=f"Injection Rate – {selected}")
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.line(wdf, x="Date", y="WHP", title=f"WHP Trend – {selected}")
    st.plotly_chart(fig2, use_container_width=True)

# In[4]:
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🛢 Producer Surveillance")

prod_file = st.file_uploader("Upload Producer Data", type=["csv", "xlsx"])

if prod_file:
    df = pd.read_csv(prod_file) if prod_file.name.endswith(".csv") else pd.read_excel(prod_file)
    st.dataframe(df.head())

    wells = df["Well"].unique()
    selected = st.selectbox("Choose Producer Well", wells)

    wdf = df[df["Well"] == selected]

    fig = px.line(wdf, x="Date", y="Oil", title=f"Oil Rate – {selected}")
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.line(wdf, x="Date", y="Watercut", title=f"Watercut – {selected}")
    st.plotly_chart(fig2, use_container_width=True)

# In[5]:
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧪 Diagnostics Module")
st.markdown("For Step Rate Tests, Falloff Tests, and Pressure Transient Evaluation")

test_file = st.file_uploader("Upload Step-Rate or Falloff Data")

if test_file:
    df = pd.read_csv(test_file)
    st.dataframe(df.head())

    if "Rate" in df.columns and "Pressure" in df.columns:
        fig = px.scatter(df, x="Rate", y="Pressure", trendline="ols",
                         title="Step-Rate Test Curve")
        st.plotly_chart(fig, use_container_width=True)

# In[6]:
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import plotly.express as px

st.title("🤖 Machine Learning")

datafile = st.file_uploader("Upload Training Dataset")

if datafile:
    df = pd.read_csv(datafile)
    st.dataframe(df.head())

    target = "Injectivity"
    features = [c for c in df.columns if c not in ["Injectivity", "Date", "Well"]]

    model = RandomForestRegressor()
    model.fit(df[features], df[target])

    st.success("✅ Model trained.")

    # Predict
    df["Prediction"] = model.predict(df[features])

    fig = px.line(df, x="Date", y=["Injectivity", "Prediction"],
                  title="Injectivity Prediction vs Actual")
    st.plotly_chart(fig, use_container_width=True)

# In[7]:
import streamlit as st
import pandas as pd

st.title("📂 Data Automation")

uploaded = st.file_uploader("Upload Data File", type=["csv", "xlsx"])

if uploaded:
    df = pd.read_csv(uploaded) if uploaded.name.endswith(".csv") else pd.read_excel(uploaded)

    st.subheader("Preview")
    st.dataframe(df.head())

    st.subheader("Clean Data")
    df_clean = df.dropna()
    st.write(df_clean.head())

    st.download_button("Download Cleaned Dataset",
                       df_clean.to_csv(index=False),
                       file_name="cleaned_data.csv")

# In[8]:
