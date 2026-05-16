from dotenv import load_dotenv 

load_dotenv()

chave=load_dotenv()

if chave:
    print("a chave foi carregada com sucesso!")
else:
    print("chave com erro de leitura!")