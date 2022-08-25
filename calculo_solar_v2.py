import streamlit as st

# para rodar no computador:
# streamlit run <nome do projeto>

st.title('CÁLCULO SOLAR')
# ------------
option = st.selectbox(
     'Selecione o tipo de cálculo',
     ('Escolha o cálculo', 'Cáculo para encontrar o KWh/mês', 'Cáculo para encontrar a Qtd de módulos', 'CÁLCULO MPPT'))

if (option == 'Cáculo para encontrar o KWh/mês'):
    st.subheader('Cáculo para encontrar o KWh/mês')

    n_cliente = st.text_input('Digite o nome do cliente:')
    wp = st.number_input('Digite a potência do Módulo:')
    qtd_mod = st.number_input('Digite a Quantidade de Módulos:')

    wp_qtdmod = wp * qtd_mod  # kwp

    rad_solar = st.number_input('Digite a Irradiação Solar:')

    result2 = wp_qtdmod * rad_solar

    result_final = ((result2 * 30) / 1000)
    porct = (result_final * 0.20)
    kwhm = result_final - porct  # kWh/mês

    st.write(""" <style> .font {font-size:20px ; font-family: 'Cooper Black'; color: red;}</style> """,
             unsafe_allow_html=True)

    if kwhm > 0:
        st.subheader('Consulmo Mensal:')
        st.write('<p class="font">Nome do cliente: {}</p> '.format(n_cliente), unsafe_allow_html=True)
        st.write('<p class="font">{}Kwh</p>'.format(round(kwhm)), unsafe_allow_html=True)
    else:
        st.write('Preencha todos os campos')

elif(option == 'Cáculo para encontrar a Qtd de módulos'):
    st.subheader('Cáculo para encontrar a Qtd de módulos')

    KWHM = st.number_input('Digite o KWh/mês:')
    pot_mod = st.number_input('Digite a potência do módulo:')
    irad_solar = st.number_input('Digite a irradiação solar:')

    if (KWHM > 0) and (pot_mod > 0) and (irad_solar > 0):
        calculoMod = KWHM / (((pot_mod * irad_solar * 0.8) * 30) / 1000)
        st.write('<p class="font">A quantidade de módulos será: {}</p>'.format(round(calculoMod)),
                 unsafe_allow_html=True)
    else:
        st.write('Preencha todos os campos')

    # CÁLCULO MPPT
elif(option == 'CÁLCULO MPPT'):
    # 1º- Entrada dados do módulo:
    st.subheader('Entre com os dados do módulo:')
    Voc = st.number_input('Digite a tensão de circuito aberto Voc:')  # tensão circuito aberto
    Temp = st.number_input('Digite a temperatura(menor do ano:)')
    stc = st.number_input('Digite o STC:')
    TcVoc = st.number_input('Digite o Coeficiente circuito aberto TcVoc(%):')  # coeficiente circuito aberto(%)
    # fórmula
    if TcVoc != 0:
        VocMax = Voc + Voc * ((Temp - stc) * (TcVoc / 100))
        st.write('Tensão de Circuito aberto Máximo', round(VocMax, 2))
        st.subheader(40 * '=')
    else:
        st.write('Preencha todos os campos')

    # 2º- Encontrar número máximo de módulos suportado por string
    VinMax = st.number_input('Digite a voltagem de entrada máxima:')
    if (VinMax != 0) and (VocMax != 0):
        modstring = VinMax / VocMax
        st.write('Nº máximo de módulos por string', round(modstring))
        st.subheader(40 * '=')
    else:
        st.write('Preencha todos os campos')

else:
    st.write('ESCOLHA UMA OPÇÃO')


# ---------------------------------------------------------------------
