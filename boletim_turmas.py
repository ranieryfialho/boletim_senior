import streamlit as st
import pandas as pd

st.title("Boletim Sênior Profissões")
st.subheader("Escolha a turma")

boletim = pd.read_csv('https://raw.githubusercontent.com/ranieryfialho/boletim_senior/main/BOLETIM%20beta.csv')
st.dataframe(boletim)

filtrar = st.selectbox("Turmas", boletim["TURMA"].unique())
botao = st.button("Filtrar")
st.write("-"*80)

if botao == True:
    boletim.loc[boletim["TURMA"] == "filtrar"]