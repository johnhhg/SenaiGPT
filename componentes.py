import streamlit as st
st.title("Secretaria SENAi Americana")
st.subheader("Conheça nossos Cursos")
st.write("I.A Generativa, Power BI, Empilhadeira, Excel, Eletrecista,  Instalador")
st.markdown ("**Atençao** : Verifique se existem vagas disponiveis")

nome = st.text_input("Digite o seu nome")
idade = st.number_input("Digite a sua idad", min_value=16, max_value=99)
cursoEscolhido = st.selectbox ("cursos disponiveis",["I.A Generativa", "Power BI", "Empilhadeira"," Excel", "Eletrecista",  "Instalador"])
aceitaTermos = st.checkbox("Ao clicar aqui, você aceita os termos e condições")

if st.button("Enviar resposta"):
  if nome and idade and cursoEscolhido and aceitaTermos:
   st.success("deu certo")
  else:
     st.error ("preencha todos os campos.")