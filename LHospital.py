from math import *
from numpy import poly1d
from numpy.polynomial import polynomial as P

x = 0
grau = 0
coeficientes = 0
result = 0

aux = 0

opcao = ''
lista_de_equacoes=[]
equacao=[]
derivada = 0
equacoes_derivadas=[]
	
x=input("O limite de f(x) tende para qual valor? ")

while opcao != 's':
	grau = input("Grau da equacao: ")

	for i in range(0, grau+1):
		coeficientes = input("Coeficiente %s: " %chr(65+i))
		equacao.append(coeficientes)
	
	lista_de_equacoes.append(poly1d(equacao))
	equacao=[]
	opcao=raw_input("Deseja Sair S/N: ")

#L'Hospital
for i in range(0, len(lista_de_equacoes)):
	derivada = lista_de_equacoes[i]
	for j in range(0, len(lista_de_equacoes[i])): 	
		aux = derivada(x)
		while (aux == 0):
			derivada=derivada.deriv()
			aux=derivada(x)
	equacoes_derivadas.append(derivada)	
	
#print equacoes_derivadas
print "Resultado :", P.polydiv(equacoes_derivadas[0](x),equacoes_derivadas[1](x))[0]

