import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 추천기", page_icon="🍽️")

st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라드립니다!")

# 추천할 점심 메뉴 리스트
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈까스",
    "국밥",
    "비빔밥",
    "짜장면",
    "짬뽕",
    "초밥",
    "라멘",
    "파스타",
    "햄버거",
    "쌀국수",
    "마라탕",
    "샌드위치",
    "샐러드",
    "떡볶이",
    "냉면",
]

# 버튼을 눌렀을 때 실행될 동작
if st.button("🎲 오늘의 메뉴 추천받기", use_container_width=True):
    selected_menu = random.choice(lunch_menus)
    st.balloons()  # 축하 풍선 효과
    st.success(f"오늘의 추천 점심 메뉴는 **{selected_menu}** 입니다! 맛있게 드세요! 😋")
