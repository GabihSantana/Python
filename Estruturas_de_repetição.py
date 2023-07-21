texto = input("Digite uma palavra: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper( ) in VOGAIS:
        print(letra, end=" ")

else:
    print( )

while True:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break

    print(opcao)
