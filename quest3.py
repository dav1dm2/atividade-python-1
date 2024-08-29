#o programa confere se o o input da letra existe em "aeiou" e se sim o informa se é uma vogal caso contrario se é uma consoante

while True:
    letras = input("digite uma letra: ")

    if letras in "aeiou":
        print("a letra é uma vogal")
        break
    elif letras in "bcdfghjklmnpqrstvwixyz":
        print("a letra é uma consoante")
        break

    else:
        print("ERRO: entrada invalida") 