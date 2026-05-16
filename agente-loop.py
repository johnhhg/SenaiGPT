from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
load_dotenv()
agente = Agent (
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)
while True:
    pergunta=input("digite sua duvida")
    if pergunta.lower() in ['exist','sair','cancelar']:
      print("fim da responta \nFaça mais uma pergunta")
      break
    else:
        agente.print_response(pergunta)