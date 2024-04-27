import streamlit as st
import pandas as pd

st.title("Boletim Sênior Profissões")
st.subheader("Escolha a turma")

turmas = st.selectbox("Turmas", ["2001-A","2002-A","2003-A","2004-A"])
# st.write(turmas)]

boletim = pd.read_csv('https://raw.githubusercontent.com/ranieryfialho/boletim_senior/main/Boletim%20de%20Todas%20as%20turmas.csv')
st.write(boletim)