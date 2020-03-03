

minha_lista = ["abacaxi","melancia","abacate","pera"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abcaxi",2,9.89]
tamanho = len(minha_lista)#esse comando veriica o tamanho da lista
print("o numero de elementos da minha_lista é de :",tamanho)
print("minha_lista contem : ",minha_lista)
print("minha_lista_2 contem:",minha_lista_2)
print("minha_lista3 contem:" ,minha_lista_3)

minha_lista.append("limao")#incluindo mais um elemento a lista
print(minha_lista)
#Fazendo uma busca na lista usando o if
if 7 in minha_lista_2:
    print("numero 7 esta na lista")
else:
     print(" o 7 nao esta na lista")

del minha_lista[2:]#esse comando elimina do segundo item em andiante
print(minha_lista)