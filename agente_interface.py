import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv
load_dotenv()
agente = Agent (model= OpenAIChat(id="gpt-4o-mini"),
 description="vocé é um professor de python", 
 tools=[DuckDuckGoTools(),WikipediaTools()],
 markdown=True              
        )  #tupla pois nao mudaremos os agentes
st.title("Agente de I.A 🤖")

pergunta = st.chat_input ("Digite sua pergunta")
if pergunta: 
    with st.chat_message ("user"):
        st.markdown(pergunta)
        with st.chat_message("assistant"):
            with st.spinner("Agente pesando..."):
             resposta = agente.run(pergunta)
             st.markdown(resposta.content)

