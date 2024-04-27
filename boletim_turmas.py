import streamlit as st
import pandas as pd

st.title("Boletim Sênior Profissões")
st.subheader("Escolha a turma")

turmas = st.selectbox("Turmas", ["2001-A","2002-A","2003-A","2004-A"])
botao = st.button("Filtrar")
# st.write(botao)

boletim = pd.read_csv('https://raw.githubusercontent.com/ranieryfialho/boletim_senior/main/BOLETIM%20beta.csv')
st.dataframe(boletim)
st.write("-"*80)

turmas_selecao = boletim["turmas"].unique()

# df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv")

# st.dataframe(df)

# linguagens = df["Linguagem"].unique()

# escolha = st.selectbox("Escolha um", linguagens)

# if st.button("Click em mim"):
#     filtro = df.loc[df["Linguagem"] == escolha]
#     st.write(filtro)