string = input("Digite a string a ser repetida: ")

try:
    numero = int(input("Digite a quantidade de vezes: "))
except ValueError:
    print("Digite um numero válido")
    pass
else:
    for i in range (numero):
        print(string)
