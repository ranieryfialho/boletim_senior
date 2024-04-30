import streamlit as st
import pandas as pd

st.title("Filtro por Aluno")
st.subheader("Escolha a turma")

boletim = pd.read_csv('https://raw.githubusercontent.com/ranieryfialho/boletim_senior/main/BOLETIM%20beta.csv')

if "boletim_filtrado_aluno" not in st.session_state:
    st.session_state.boletim_filtrado_aluno = pd.DataFrame()

filtrar_aluno = st.text_input("Digite o nome do aluno: ").strip().lower()
botao_aluno = st.button("Filtrar")

if botao_aluno:
    st.session_state.boletim_filtrado_aluno = boletim[boletim["ALUNOS"].str.lower().str.contains(filtrar_aluno)]
    st.dataframe(st.session_state.boletim_filtrado_aluno) 

if not st.session_state.boletim_filtrado_aluno.empty:
    aluno_selecionado = st.selectbox("Selecione um aluno para ver as notas", st.session_state.boletim_filtrado_aluno['ALUNOS'].unique())
    botao_notas = st.button('Mostrar Gráfico de Notas')
    
    if botao_notas:
        notas_aluno = boletim.loc[boletim['ALUNOS'].str.lower() == aluno_selecionado.lower(), ['IRS', 'CRD', 'CTF', 'APG', 'PTS', 'ILT',
                                                                                            'ADM', 'DP', 'SCT', 'CONT', 'TCC']]
        st.bar_chart(notas_aluno.T) 
