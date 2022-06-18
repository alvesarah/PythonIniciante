minha_variavel = "ola"

#FOR -> para
for caracter in minha_variavel: #Para cada caracter dentro da minha_variavel faça:
    print(caracter)

#Listas de forma automática (Criar lista de 0 a 10)
range(0, 10) #(start = 0, stop = ?, step = 1)

list(range(11)) #cria a lista
set(range(11))
tuple(range(11))

#Números ímpares R:Começa no 1 e acaba no 9
list(range(1, 10, 2))

#Números pares
numeros_pares = list(range(0, 11, 2))

#Multiplicar números ao quadrado
for numero in numeros_pares:
    print(numero ** 3)

#While -> enquanto
x = 0
while x <= 10:
    print(x ** 3)
    x += 2 #incrementar

usuario_quiser = True

while usuario_quiser == True:
    usuario_input = input("Quer continuar? (S/N)")
    if usuario_input == "N":
        usuario_quiser = False
    print("continue")