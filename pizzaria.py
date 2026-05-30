import streamlit as st
st.title("Bem vindo a Pizzaria Dipadre🍕")
st.image("pizza.jpg")
st.subheader("Conheça nosso sabores")
st.write ("Calabresa, Margherita, Portuguesa, Quatro Queijos")

nome=st.text_input("Digite o seu nome:")
cidade=st.text_input("Digite sua cidade")
bairro=st.text_input("Digite seu bairro")
saboresEscolhidos = st.selectbox("sabores diponiveis,",["Calabresa", "Margherita", "Portuguesa", "Quatro Queijos"])

if st.button("Enviar resposta"):
    if nome and cidade and bairro:
        st.success("informarçoes salvas")
    else:
     st.error ("dados incompletos")