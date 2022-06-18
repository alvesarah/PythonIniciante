notas = [3, 5, 6, 4, 8]

notas.append(10) #Adicionar mais uma nota
notas.append(8) #Adicionar mais uma nota

print(notas)

#Calcular média
len(notas) #quantos elementos tem
sum(notas) #somar as notas

sum(notas)/len(notas)

#método que calcula média
def media_notas(notas):
    return print(round(sum(notas)/len(notas), 1))

media_notas(notas)

notas[0] #acessar o index 0 R:3

#último index da lista
notas[-1] #ou
notas[len(notas)-1] # R:8

#Tuplas (Como a lista, porém os valores devem estar entre parenteses. O valor não pode ser MODIFICADO, set não suporta index, ou seja, não tem ordem correta)
tupla = (3, 4, 5) #(3, 4, 5)

tupla += (4, ) #Adicionando um elemento a tupla, a virgula deve estar no final (3, 4, 5, 4)

#Sets (Parecido com a tupla, porém os valores são colocados entre chaves. Não pode ter valores repetidos e são desordenados)
set_nota = {1, 2, 3, 4, 5}

set_nota_repetindo = {1, 2, 3, 4, 5, 5, 3, 2, 4} # R: {1, 2, 3, 4, 5}

set_nota.add(6) #adicionar mais um, se adicionar um que já tem na lista, ele não adiciona