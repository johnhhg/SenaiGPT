import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

personalidade = st.sidebar.selectbox ("personalidade",["Professor de python","Professor de historia","Cientista maluco"])

descricao = {
    "Professor de python":"voce é um professor de python que responde com exemplos e contexto",
    "Professor de historia":"voce é um professor de historia que sempre explica de forma clara e exata",
    "Cientista maluco":"voce é um cientista maluco que sempre esta em busca  de noavs inovaçes e projetos" }
                                      
agente = Agent(
    model= OpenAIChat(id="gpt-4o-mini"),
    description=descricao[personalidade], 
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True                                 
)

if "mensagens" not in st.session_state:
     st.session_state.mensagem = []
     
for msg in st.session_state.mensagem: 
         with st.chat_message(msg["role"]):
          st.markdown(msg["content"])

if st.sidebar.button("limpar conversa"):
    st.session_state.mensagem =[]
    st.rerun()

st.title("Sistema multiAgentes")

pergunta = st.chat_input("digite sua mensagem")    

if pergunta: 
        with st.chat_message("user"):
            st.markdown(pergunta)
            st.session_state.mensagem.append({"role":"user","content":pergunta})
        with st.chat_message("assistant"):
         resposta = agente.run(pergunta)
         st.markdown(resposta.content)
    
        st.session_state.mensagem.append({"role": "assistant", "content": resposta.content})