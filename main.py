import streamlit as st
import pandas as pd

st.set_page_config(page_title="🎨 명화 탐색기", layout="wide")

st.title("🎨 명화 탐색기 (MET Museum API)")

# 데이터 불러오기
csv_url = "https://raw.githubusercontent.com/사용자이름/저장소이름/main/art_data.csv"
df = pd.read_csv(csv_url)

# 검색어 입력창 만들기
search_term = st.text_input("검색어를 입력하세요 (작품명 또는 작가명)", "")

# 검색어가 있을 때 필터링
if search_term:
    # 대소문자 구분 없이 제목 또는 작가명에 검색어 포함된 행만 필터링
    filtered_df = df[df["Title"].str.contains(search_term, case=False, na=False) | 
                     df["Artist"].str.contains(search_term, case=False, na=False)]
else:
    filtered_df = df

# 결과 보여주기
if filtered_df.empty:
    st.write("검색 결과가 없습니다.")
else:
    for i, row in filtered_df.iterrows():
        st.subheader(row["Title"])
        st.image(row["Image"])
        st.markdown(f"""
        - 👨‍🎨 **작가:** {row['Artist']}  
        - 📅 **연도:** {row['Date']}  
        - 🎨 **재료:** {row['Medium']}
        """)
        st.markdown("---")
