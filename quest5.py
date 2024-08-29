#o programa compara 2 vezes as condições  antes de cair no else para determinar o "maior_numero" e aquele que se encaixar
# é mostrado para o ususario


print("vou dizer-lo qual de 3 numeros é o maior numero :)\n")

while True:
    num_1 = input("digite o primeiro numero: ")
    num_2 = input("digite o segundo numero: ")
    num_3 = input("digite o terceiro numero: ")

    try:
        if float(num_1) >= float(num_2) and float(num_1) >= float(num_3):
            maior_num = float(num_1)

        elif float(num_2) >= float(num_1) and float(num_2) >= float(num_3):
            maior_num = num_2

        else:
            maior_num = num_3
        print(f"\no numero {maior_num} é o maior numero :) ")
        break

    except ValueError:
        print("\nError valor não numerico")