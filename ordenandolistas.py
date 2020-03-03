lista = [124,345,5,72,46,6,7,3,1,7,0]
print("lista desordenada")
print (lista)
lista.sort()#esse metodo faz a ordenacao da lista
print("Lista Ordenada")
print(lista)

lista1 = [40,39,33,20,11,5,8,2,1]
print("lista1 desordenada")
print(lista1)
print("lista1 ordenada pelo metodo sorted")
lista1 = sorted(lista1)#esse metodo faz a ordenaçao e o resultado vem como retorno
print(lista1)

lista.sort(reverse=True)
print("lista revertida")
print(lista)
