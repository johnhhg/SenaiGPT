from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
#todos os agente necessitam de uma chave api, e afuçao load_dotenv faz a leitura do arquivo do .env.
load_dotenv()

agente=Agent(
       model=OpenAIChat(id="gpt-4o-mini"),
       markdown=True
)
# agente.print_response ("ME conte uma curiosida")

pergunta=input("me responda uma duvida")
agente.print_response(f"{pergunta}")
