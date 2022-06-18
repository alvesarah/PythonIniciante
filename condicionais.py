devo_continuar = True

if devo_continuar == True:
    print("Continue")
#Não é necessário o uso do "== True"
if devo_continuar:
    print("Continue")

pessoas_conhecidas = ["João", "Maria", "Ana", "Fabio"]

# pessoa = input("Entre com o nome de uma pessoa")

pessoa = 4

#Forma explicativa
if pessoa in pessoas_conhecidas:
    print("Você conhece essa pessoa")

if pessoa not in pessoas_conhecidas:
    print("Você não conhece essa pessoa")

#Forma melhorada
if pessoa in pessoas_conhecidas:
    print("Você conhece essa pessoa")
else:
    print("Você não conhece essa pessoa")

if pessoa in pessoas_conhecidas:
    print("Você conhece {}".format(pessoa)) #coloca o nome da pessoa
else:
    print("Você não conhece "+str(pessoa)) #concatenar(só serve se for string, para imprimir um int, deve-se transforma-lo em str) o nome da pessoa