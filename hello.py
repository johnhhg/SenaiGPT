import streamlit as st
st.title("Bem vindo á minha primeira pagina WEB")
st.subheader("desenvolvido por : Lucas")

nome=st.text_input("Digite seu nome:")
email=st.text_input("Digite seu email")
if st.button("cadastrar"):
 if nome and email:
    st.success(f" email digitado com sucesso")
 else:
      st.error("falta dados")
 

if nome:
    st.write(f"Bem vindo{nome}")
    st.balloons()
