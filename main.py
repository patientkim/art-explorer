import streamlit as st
import pandas as pd

st.set_page_config(page_title="🎨 명화 탐색기", layout="wide")

st.title("🎨 명화 탐색기 (MET Museum API)")

# GitHub에 올린 CSV 데이터 불러오기
csv_url = "https://raw.githubusercontent.com/patientkim/art-explorer/main/art_data.csv"
df = pd.read_csv(csv_url)

# 작품 목록 보여주기
for i, row in df.iterrows():
    st.subheader(row["Title"])
    st.image(row["Image"])
    st.markdown(f"""
    - 👨‍🎨 **작가:** {row['Artist']}  
    - 📅 **연도:** {row['Date']}  
    - 🎨 **재료:** {row['Medium']}
    """)
    st.markdown("---")
