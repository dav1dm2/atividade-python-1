
#o codigo determina se o numero digitado é impar ou par

while True:
    numero = input("digite um numero: ")

    try:
        if(int(numero) % 2 == 0): 
            print(f"\o numero {numero} é par")
            break
        elif(int(numero) % 2 != 0 ):
            print(f"\no numero {numero} é impar")
            break
    
    except ValueError:
        print("\nErro: valor nao numerico!")