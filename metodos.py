#criando o próprio método
def meu_metodo():
    print("Olá método")

meu_metodo()

#criando o próprio método
def meu_metodo_parte_dois():
    print("Olá")
    print("Método")
print("Fora do método") #Se não houver identação, ele sairá do método

meu_metodo_parte_dois()

def soma_dois_valores(valor1, valor2):
    return valor1 + valor2

soma_dois_valores(2, 5)

#Built In - Inbutidas (Funções que o python já tem)

print("Olá") #imprime algo

int(10.3) #transforma o valor em inteiro

float(10) #transforma o valor em float

len("Olá") #Diz quantos caracteres tem

x = -10
abs(x) #Se x é negativo, qual valor absoluto de x ou qual o módulo de x? R: 10

lista = [1, 2, 3, 4]
sum(lista) #Soma a lista
min(lista) #Valor menor da lista
max(lista) #Valor máximo da lista

round(10.90) #Arredonda para 11
round(10.20) #Arredonda para 10
round(10.50) #Arredonda para 10
round(10.4837484, 2) #Quantas casas decimais quer arredondar R:10.48