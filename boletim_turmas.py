import streamlit as st
import pandas as pd

st.title("Boletim Sênior Profissões 👽")
st.subheader("Escolha a turma")

boletim = pd.read_csv('https://raw.githubusercontent.com/ranieryfialho/boletim_senior/main/BOLETIM%20beta.csv')
st.dataframe(boletim)

filtrar_turma = st.selectbox("Turmas", boletim["TURMA"].unique())
botao_turma = st.button("Filtrar por Turma")

filtar_aluno = st.text_input("Digite o nome do aluno: ")
botao_aluno = st.button("Filtrar por Aluno")
st.write("-"*80)

if botao_turma:
    boletim_filtrado_turma = boletim.loc[boletim["TURMA"] == filtrar_turma]
    st.dataframe(boletim_filtrado_turma)

if botao_aluno:
    boletim_filtrado_aluno = boletim.loc[boletim["ALUNOS"] == filtar_aluno]
    st.dataframe(boletim_filtrado_aluno)