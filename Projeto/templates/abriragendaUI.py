import streamlit as st
from views import View
import time

class AbrirAgendaUI:
    def main():
        st.header("Abrir Agenda do Dia")
        data = "30/10/2024"
        inicio = "08:00"
        fim = "12:00"
        intervalo = 30
        View.horario_abrir_agenda(data, inicio, fim, intervalo)