import streamlit as st
from views import View
import time

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            p = View.profissional_autenticar(email, senha)
            if c == None and p == None: 
                st.write("E-mail ou senha inválidos")
            if c != None:    
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.session_state["tipo"] = "cliente"
                st.rerun()
            if p != None:    
                st.session_state["cliente_id"] = p["id"]
                st.session_state["cliente_nome"] = p["nome"]
                st.session_state["tipo"] = "profissional"
                st.rerun()                
