import streamlit as st
import requests
import pandas as pd
import plotly.express as px

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI BI Copilot", layout="wide")

st.title("📊 AI Business Intelligence Copilot")

# -------------------------
# UPLOAD SECTION
# -------------------------
st.header("1. Upload Dataset")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}

    response = requests.post(f"{BASE_URL}/upload", files={"file": uploaded_file})

    if response.status_code == 200:
        data = response.json()
        st.success("Dataset uploaded successfully!")
        st.json(data)
    else:
        st.error("Upload failed")

# -------------------------
# QUERY SECTION
# -------------------------
st.header("2. Ask Questions")

question = st.text_input("Ask something about your data:")

if st.button("Analyze"):
    if question:

        response = requests.post(
            f"{BASE_URL}/analyze",
            json={"question": question}
        )

        if response.status_code == 200:
            result = response.json()

            st.subheader("📊 Data")
            st.dataframe(pd.DataFrame(result["data"]))

            df = pd.DataFrame(result["data"])

            if len(df) > 0 and len(df.columns) >= 2:

                numeric_cols = df.select_dtypes(include=["number"]).columns
                text_cols = df.select_dtypes(include=["object"]).columns

                if len(numeric_cols) > 0 and len(text_cols) > 0:

                    fig = px.bar(
                        df,
                        x=text_cols[0],
                        y=numeric_cols[0],
                        title="📊 AI Generated Insight Chart"
                    )

                    st.plotly_chart(fig)

            st.subheader("🧠 Insights")
            for i in result["insights"]:
                st.write("•", i)

        else:
            st.error("Analysis failed")