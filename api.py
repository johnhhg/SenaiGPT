# instalar biblioteca
#pip install  request

#SEGUNDO PASSO:ADICIONAR/IMPORT 
import requests
nome = input ("digite seu nome")
email = input ("digite seu e-mail")
telefone = ("digite seu telefone")


#recebe o cep digitado pelo usuario
digite= input("digite seu cep: ")

url= f"https://viacep.com.br/ws/{digite}/json/" 
dados =  requests.get(url).json()
print (f"bem vindo ao mercado livre {nome}! o seu e-mail é {email}. O seu telefone é {telefone} Voce mora na rua {dados['localidade']}, no estado de {dados ['estado']}")



# rua= dados ['logradouro']
# bairro=['bairro']
# cidade=dados['localidade']
# #atribuindo variaveis
# print(rua)
# print(bairro)
# print(localidade)
