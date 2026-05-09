listaNotas= []

print("-" * 40)
print("bem vindo a I.A que calcula notas e média final")
while True:
    notas=input("digite as notas que deseja (digite sair para parar)")
    if notas.lower()=="sair":
        break
    else:
        listaNotas.append(float(notas))
print(listaNotas)
media=sum(listaNotas) / len (listaNotas)

if media >=7:
  print ("aprovado🥳")
else:
    print("reprovado😞")
print(f"a media final do aluno é {media:.2f}")
