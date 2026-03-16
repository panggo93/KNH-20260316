import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 텍스트/마크다운
st.header("1. 텍스트/마크다운")
st.subheader("Streamlit 주요 요소 데모")
st.markdown("**마크다운**과 $\LaTeX$ 수식 지원: $E=mc^2$")
st.code("print('Hello, Streamlit!')", language="python")

# 데이터 표시
import pandas as pd
import numpy as np
st.header("2. 데이터 표시")
df = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
st.dataframe(df)
st.table(df.head(3))
st.json({"key": "value", "list": [1,2,3]})

# 차트/그래프
st.header("3. 차트/그래프")
st.line_chart(df)
st.bar_chart(df)

# 입력 위젯
st.header("4. 입력 위젯")
name = st.text_input("이름을 입력하세요:")
age = st.number_input("나이", min_value=0, max_value=120, value=25)
agree = st.checkbox("동의합니다")
color = st.selectbox("좋아하는 색상", ["빨강", "초록", "파랑"])
if st.button("입력 완료"):
    st.write(f"안녕하세요, {name}님! 나이: {age}, 색상: {color}, 동의여부: {agree}")

# 미디어
st.header("5. 미디어")
st.image("https://static.streamlit.io/examples/cat.jpg", caption="고양이 이미지", width=200)

# 레이아웃/구조
st.header("6. 레이아웃/구조")
col1, col2 = st.columns(2)
with col1:
    st.write("왼쪽 컬럼")
with col2:
    st.write("오른쪽 컬럼")
with st.expander("더보기"):
    st.write("이곳은 확장 영역입니다.")

# 상태/상호작용
st.header("7. 상태/상호작용")
if 'count' not in st.session_state:
    st.session_state['count'] = 0
if st.button("카운트 증가"):
    st.session_state['count'] += 1
st.write(f"카운트: {st.session_state['count']}")

# 기타
st.header("8. 기타")
with st.spinner("로딩 중..."):
    st.success("완료!")
