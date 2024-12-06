import streamlit as st
import pandas as pd
from views import View
import time

class MeusDadosUI:
    def main():
        st.header("Meus Dados")
        MeusDadosUI.atualizar()

    def atualizar():
        op = View.cliente_listar_id(st.session_state["cliente_id"])
        perfis = View.perfil_listar()
        nome = st.text_input("Informe o novo nome", op.nome)
        email = st.text_input("Informe o novo e-mail", op.email)
        fone = st.text_input("Informe o novo fone", op.fone)
        senha = st.text_input("Informe a nova senha", op.senha, type="password")
        id_perfil = None if op.id_perfil in [0, None] else op.id_perfil
        perfil = st.selectbox("Informe o novo perfil", perfis, next((i for i, c in enumerate(perfis) if c.id == id_perfil), None))
        if st.button("Atualizar"):
            View.cliente_atualizar(op.id, nome, email, fone, senha, perfil.id)
            st.success("Dados atualizado com sucesso")
            time.sleep(2)
            st.rerun()
