import streamlit as st

st.write(st.session_state)
nome = st.text_input("Nome", key="usuário")
st.write(st.session_state)
senha = st.text_input("Senha")
if st.button("Entrar"):
    st.write(st.session_state)
