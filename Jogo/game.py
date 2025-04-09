import random
user = input("Escolha seu elemento para jogar 1- Pedra, 2- Papel e 3- Tesoura com a máquina: ")
maquina = random.randrange(1, 3)
print(maquina)
if maquina == 1 and user == 1:
    print("Empatou, tente outra vez!")
elif maquina == 1 and user == 2:
    print("Usuario foi o vencedor!")
elif maquina == 1 and user == 3:
    print("A maquina venceu!")
elif maquina == 2 and user == 1:
    print("A maquina venceu!")
elif maquina == 2 and user == 2:
    print("Empatou, tente outra vez!")
elif maquina == 2 and user == 3:
    print("A usuário venceu!")
elif maquina == 3 and user == 1:
    print("Usuario foi o vencedor!")
elif maquina == 3 and user == 2:
    print("A maquina venceu")
else:
    print("Empatou, tente outra vez!")
