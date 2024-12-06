from templates.manterclienteUI import ManterClienteUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterperfilUI import ManterPerfilUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.abrircontaUI import AbrirContaUI
from templates.listarhorarioUI import ListarHorarioUI
from templates.loginUI import LoginUI
from templates.meusdadosUI import MeusDadosUI
from templates.meusdadosprofissionalUI import MeusDadosProfissionalUI
from templates.minhaagendaUI import MinhaAgendaUI
from views import View

import streamlit as st

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
               
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Perfis", "Cadastro de Profissionais", "Cadastro de Serviços", "Abrir Agenda do Dia", "Meus Dados"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Perfis": ManterPerfilUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
        if op == "Meus Dados": MeusDadosUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Horários Disponíveis", "Meus Dados"])
        if op == "Horários Disponíveis": ListarHorarioUI.main()
        if op == "Meus Dados": MeusDadosUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Minha Agenda", "Meus Dados"])
        if op == "Minha Agenda": MinhaAgendaUI.main()
        if op == "Meus Dados": MeusDadosProfissionalUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()
    
    def sidebar():
        if "cliente_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["cliente_nome"] == "admin"
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            # menu do usuário
            if st.session_state["tipo"] == "cliente":
                if admin: IndexUI.menu_admin()
                else: IndexUI.menu_cliente()
            else:
                IndexUI.menu_profissional()    
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
    
    def main():
        # verifica a existe o usuário admin
        View.cliente_admin()
        # monta o sidebar
        IndexUI.sidebar()
       
IndexUI.main()
