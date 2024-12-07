
import streamlit as st
st.title("인공지능 시인")
sub = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " +sub)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        st.write()
