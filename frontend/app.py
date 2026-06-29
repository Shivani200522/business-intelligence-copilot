import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Business Intelligence Copilot",
    page_icon="📊",
    layout="wide"
)

with st.sidebar:
    selected = option_menu(
        "AI BI Copilot",
        ["Dashboard", "Upload Dataset", "Analyze Data"],
        icons=["bar-chart", "cloud-upload", "robot"],
        default_index=0,
    )

st.title("📊 AI Business Intelligence Copilot")

# -------------------------
# UPLOAD SECTION
# -------------------------
st.header("1. Upload Dataset")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
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
            df = pd.DataFrame(result["data"])

            # --- Query Results ---
            st.subheader("📊 Query Results")
            st.dataframe(df, use_container_width=True)

            # --- KPI Cards ---
            col1, col2, col3 = st.columns(3)
            col1.metric("Rows", len(df))
            col2.metric("Columns", len(df.columns))

            numeric_cols = df.select_dtypes(include=["number"]).columns
            if len(numeric_cols) > 0:
                col3.metric("Average", round(df[numeric_cols[0]].mean(), 2))
            else:
                col3.metric("Average", "-")

            # --- Visualization ---
            if len(df) > 0:
                numeric_cols = df.select_dtypes(include=["number"]).columns
                category_cols = df.select_dtypes(exclude=["number"]).columns

                if len(numeric_cols) > 0 and len(category_cols) > 0:
                    st.subheader("📈 Visualization")
                    fig = px.bar(
                        df,
                        x=category_cols[0],
                        y=numeric_cols[0],
                        text=numeric_cols[0],
                        title=f"{numeric_cols[0]} by {category_cols[0]}"
                    )
                    st.plotly_chart(fig, use_container_width=True)

            # --- AI Insights ---
            st.subheader("🧠 AI Insights")
            st.subheader("📄 Executive Summary")
            st.success(result["summary"])
            for insight in result["insights"]:
                st.info(insight)

            # --- Download Results ---
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "⬇ Download Results",
                csv,
                "results.csv",
                "text/csv"
            )

        else:
            st.error("Analysis failed")
