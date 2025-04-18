
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="📊 Variance Analyzer", layout="centered")
st.title("📊 Variance Analysis Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file with 'Category', 'Budget', 'Actual'", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Calculate variance
    df['Variance ($)'] = df['Actual'] - df['Budget']
    df['Variance (%)'] = ((df['Actual'] - df['Budget']) / df['Budget']) * 100
    df['Direction'] = df['Variance ($)'].apply(lambda x: 'Increase' if x > 0 else 'Decrease' if x < 0 else 'No Change')

    st.subheader("📋 Variance Table")
    st.dataframe(df.style.applymap(lambda val: 'color: red' if isinstance(val, str) and val == 'Decrease' else 'color: green' if val == 'Increase' else ''))

    st.subheader("📈 Variance Bar Chart")
    df_sorted = df.sort_values(by='Variance ($)', key=abs, ascending=False)

    fig, ax = plt.subplots()
    bars = ax.bar(df_sorted['Category'], df_sorted['Variance ($)'], color=['green' if x > 0 else 'red' for x in df_sorted['Variance ($)']])
    ax.set_ylabel("Variance ($)")
    ax.set_title("Top Positive/Negative Variance by Category")
    ax.axhline(0, color='black', linewidth=0.8)
    st.pyplot(fig)

    st.subheader("⬇️ Download Analysis")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="variance_analysis.csv", mime='text/csv')

else:
    st.info("Upload a CSV file to begin analysis. Need an example?")
    st.download_button("Download Sample CSV", data=open("financials_demo.csv", "rb").read(), file_name="financials_demo.csv")
