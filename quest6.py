#o prorgrama informa 3 possiveis opções de entrada ao usuario aceitaveis para mostrar a recepção
#repetindo caso uma entrada não desejada seja digitada

print("ola digite a letra correspondente ao seu turno de estudos :)\n")
 
while True:
    turno = input(" M para matutino\n V para vespertino\n N para noturno\n\n").lower()

    if turno in "m":
        print("Bom dia :)")
        break

    elif turno in "v":
        print("Bom tarde :)")
        break

    elif turno in "n":
        print("Boa noite :)")
        break

    else:
        print("\nError: entrada invalida")     

