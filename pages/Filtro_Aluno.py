import streamlit as st
import pandas as pd

st.title("Filtro por Aluno")
st.subheader("Escolha a turma")

boletim = pd.read_csv('https://raw.githubusercontent.com/ranieryfialho/boletim_senior/main/BOLETIM%20beta.csv')
# st.dataframe(boletim)

filtar_aluno = st.text_input("Digite o nome do aluno: ").strip().lower()
botao_aluno = st.button("Filtrar por Aluno")

if botao_aluno:
    boletim_filtrado_aluno = boletim.loc[boletim["ALUNOS"].str.lower().str.contains(filtar_aluno)]
    st.dataframe(boletim_filtrado_aluno)