# import pandas as pd
# import plotly.express as px
import streamlit as st

# para rodar no computador:
# streamlit run <nome do projeto>

st.title('CÁLCULO SOLAR')

st.subheader('Cáculo para encontrar o KWh/mês')

n_cliente = st.text_input('Digite o nome do cliente:')
wp = st.number_input('Digite a potência do Módulo:')
qtd_mod = st.number_input('Digite a Quantidade de Módulos:')

wp_qtdmod = wp * qtd_mod # kwp

rad_solar = st.number_input('Digite a Irradiação Solar:')

result2 = wp_qtdmod * rad_solar

result_final = ((result2 * 30)/1000)
porct = (result_final * 0.20)
kwhm = result_final - porct # kWh/mês

st.write(""" <style> .font {font-size:20px ; font-family: 'Cooper Black'; color: red;}</style> """, unsafe_allow_html=True)

if kwhm > 0:
    st.subheader('Consulmo Mensal:')
    st.write('<p class="font">Nome do cliente: {}</p> '.format(n_cliente), unsafe_allow_html=True)
    st.write('<p class="font">{}Kwh</p>'.format(round(kwhm)), unsafe_allow_html=True)
else:
    st.write('Preencha todos os campos')

# ---------------------------------------------------------------------
st.subheader(20 * '=')

st.subheader('Cáculo para encontrar a Qtd de módulos')


KWHM = st.number_input('Digite o KWh/mês:')
pot_mod = st.number_input('Digite a potência do módulo:')
irad_solar = st.number_input('Digite a irradiação solar:')


if (KWHM > 0) and (pot_mod > 0) and (irad_solar > 0):
    calculoMod = KWHM/(((pot_mod * irad_solar * 0.8)*30)/1000)
    st.write('<p class="font">A quantidade de módulos será: {}</p>'.format(round(calculoMod)), unsafe_allow_html=True)
else:
    st.write('Preencha todos os campos')
