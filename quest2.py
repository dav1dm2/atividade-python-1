#o programa cofere e determina qual numero dos inputs é maior, e então informa ao usuario qual deles é
#em caso de erro é informado ao usuario o problema

while True:
    numero1 = input("digite um numero: ")
    numero2 = input("digite o segundo numero: ")

    try:

        if float(numero1) > float(numero2):
            print(f"\no numero {numero1} é maior ")
            break
        elif float(numero1) == float(numero2): 
            print("\nos numeros são iguais")
            break
        elif float(numero1) < float(numero2):
            print(f"\no numero {numero2} é maior")
            break

    except ValueError :
        print("\nERRO: valores não numericos")