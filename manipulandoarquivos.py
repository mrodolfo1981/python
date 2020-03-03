#manipulaçao de arquivos 


# -*- coding: utf-8 -*-

arquivo = open("arquivo.txt")

linha = arquivo.readlines() # lendo as linhas do arquivo
print(linha)

texto_completo = arquivo.read() #lendo todo o arquivo
print(texto_completo)

w = open("arquivo2.txt","a") #criando uma aquivo em branco caso abra ele apaga o q tinha antes usando o w se usar o a as linhas vao sendo incrementadas

w.write("Esse é o o meu arquivo\n")# inserido o texto entre() no arquivo
w.close()#comando que fecha o arquivo

