print("\t BEM VINDO PROFESSOR")

notaUm=float(input("digite a primeira nota do aluno:"))
notaDois=float(input("digite a primeira nota do aluno:"))
notaTres=float(input("digite a primeira nota do aluno:"))
notaQuatro=float(input("digite a primeira nota do aluno:"))

media=(notaUm + notaDois + notaTres + notaQuatro) /4
print(f"a media é {media}")
if media >=6:
    print("parabens voce esta aprovado!")
else:
    print("voce esta reprovado lamento")
