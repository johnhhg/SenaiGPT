from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools 
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv
load_dotenv()
agente = Agent (
    model=OpenAIChat(id="gpt-4o-mini"),
    description="VOCE É UM AGENTE PESQUISADOR DE ULTIMAS NOTICIAS DO MUNDO DO FUTEBOL, QUE ULTILIZA A WEB PARA TRAZER AS ULTIMAS NOTICIAS",
   add_history_to_context=True,
    tools = [DuckDuckGoTools(),TavilyTools()],
    markdown=True
)
while True:
    pergunta=input("digite sua duvida: ")
    if pergunta.lower() in ['exist','sair','cancelar']:
      print("fim da responta \nFaça mais uma pergunta")
      break
    else:
        agente.print_response(pergunta)