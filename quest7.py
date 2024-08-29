#o pro

score = 0

print("Vamos saber seu envolvimento com a vítima >:(\n")
print("Responda as seguintes perguntas com S ou N\n")

def ask_pergunta(pergunta):
    while True:
        resposta = input(pergunta + " (S/N): ").upper()
        if resposta in ['S', 'N']:
            return resposta
        else:
            print("Resposta inválida")

# Questao 1
resposta = ask_pergunta("Telefonou para a vítima?\n")
if resposta == 'S':
    score += 1 

# Questao 2
resposta = ask_pergunta("esteve no local do crime?\n")
if resposta == 'S':
    score += 1  

# Questao 3
resposta = ask_pergunta("Mora perto da vítima?\n")
if resposta == 'S':
    score += 1  

# Questao 4
resposta = ask_pergunta("DEVIA PARA A VÍTIMA?\n")
if resposta == 'S':
    score += 1 

# Questao 5
resposta = ask_pergunta("ja trabalhou com a vítima?\n")
if resposta == 'S':
    score += 1 

if score == 5:
    print("ASSASINO!!!!!!!! >>:(")
elif score >= 4 or score == 3:
    print("cumplice !!!!")
elif score == 2:
    print("SUS OMONGUS!! VENT TUM TUM TUM TUM SUS")
else:
    print("inocente :)")


print(f"culpometro marcou: {score}")
