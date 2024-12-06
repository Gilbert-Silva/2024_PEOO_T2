import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class MinhaAgendaUI:
    def main():
        st.header("Cadastro de Horários")
        MinhaAgendaUI.listar()

    def listar():
        horarios = View.horario_pesquisar(st.session_state["cliente_id"])
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:  
            dic = []
            #for obj in Horarios: dic.append(obj.__dict__)

            for obj in horarios:
                cliente = View.cliente_listar_id(obj.id_cliente)
                servico = View.servico_listar_id(obj.id_servico)
                profissional = View.profissional_listar_id(obj.id_profissional)
                if cliente != None: cliente = cliente.nome
                if servico != None: servico = servico.descricao
                if profissional != None: profissional = profissional.nome
                
                dic.append({"id" : obj.id, "data" : obj.data, "confirmado" : obj.confirmado, "cliente" : cliente, "serviço" : servico, "profissional" : profissional })
            
            df = pd.DataFrame(dic)
            st.dataframe(df)

