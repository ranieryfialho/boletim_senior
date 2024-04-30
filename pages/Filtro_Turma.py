import streamlit as st
import pandas as pd

st.title("Filtro por Turmas")
st.subheader("Escolha a turma")

boletim = pd.read_csv('https://raw.githubusercontent.com/ranieryfialho/boletim_senior/main/BOLETIM%20beta.csv')
# st.dataframe(boletim)

filtrar_turma = st.selectbox("Turmas", boletim["TURMA"].unique())
botao_turma = st.button("Filtrar por Turma")

if botao_turma:
    boletim_filtrado_turma = boletim.loc[boletim["TURMA"] == filtrar_turma]
    st.dataframe(boletim_filtrado_turma)