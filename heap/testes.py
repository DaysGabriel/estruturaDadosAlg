def swap(elem1, elem2):
    temp = elem1
    elem1 = elem2
    elem2 = temp

def swapLista(lista, index1, index2):
    temp = lista[index1]
    lista[index1] = lista[index2]
    lista[index2] = temp

lista = [1,2,3,4,5]
swap(lista[0], lista[4])
print("Lista após o 'swap' simples:",lista)

swapLista(lista, 0, 4)
print("Lista após o 'swap' próprio da lista:",lista)

lista2 = []
lista2.append(lista.pop())
print(lista2)
print(lista)