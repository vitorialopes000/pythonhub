import os
os.system("cls")

#continuação input com int e float
#int() -> converte para inteiro
#float() -> converte para não quebrado

# numero = 10
# numero2  = input("digite um numero: ")
# print("o tipo de numero é,", type(numero2))
# soma = numero + int(numero2) 
# print(f"soma de {numero} + {numero2} = ", soma)

# exenpro2 
# num1 = input("digite um numero: ")
# soma = float(num1) + 15
# print("a soma de", num1 , "+", "15" ,"=", soma)

#exemplo3 
# n1 = input("digite um numero: ")
# n2 =input("digite outro numero: ")

#soma = float(n1)+float(n2)

#print(f"a soma de {n1} + {n2} = ", soma)

#exercicios 
#atividade1

# print("*********atividade1*********")
# numero1 =input("digite um numero: ")
# numero2 =input("digite outro numero: ")
# multiplicacao = float(numero1)*float(numero2)
# print(f"a multiplicacao de {numero1} * {numero2} = ", multiplicacao)

# atividade2
# print("*********atividade2*********")
# numero = int(input("digite um numero: "))
# antecessor = numero - 1
# sucessor = numero + 1
# print(f"o antecessor de {numero} {antecessor}")
# print(f"o sucessor de {numero} {sucessor}")

#atividade3

# print("*********atividade3*********")
# numero1 = 2025
# numero2 =input("digite o ano em que voce nasceu: ")
# subtracao = float(numero1)-float(numero2)
# print(f"sua idade {numero1} - {numero2} = ", subtracao)

#porcentagem 
#print("25% de 100 =", 0.25 * 100)
#print("4% de 400 =", 0.04 * 400)
#print("99% de 1525 =", 0.99 * 1525)

#supondo que o pruduto custa 150 reais
#e o caixa deu um custo de 15%
#exemplo = float(input("digite o preco do produto "))
#desconto = 0.15 * exemplo
#print("o preco do produdo com 15% de desconto ", exemplo-desconto)

# escreva um programa de python que leia 2 itens de um supermercado, voce deve armazenar 
# onome do valor do item, no final aplique 1& de desconto no primeiro item de 25% de desconto 
# no segundo item
# calcule o valor total da compra e mostre o nome e o valor com desconto de cada item.

#exercicio desconto
print("================supermercado================")

primeiro = input("digite o nome do primeiro produdo: ")
produto1 = float(input("digite o valor do produto: "))
segundo = input("digite o nome do segundo produdo: ")
produto2 = float(input("digite o valor do produto: "))



print("====================caixa====================")

desconto1 = 0.10 * produto1
print("o preco do produto com 10% de desconto", produto1-desconto1)
desconto2 = 0.25 * produto2
print("o preco do produto com 25% de desconto", produto2-desconto2)
valorfinal1 = round(produto1-desconto1,2)
valorfinal2 = round(produto2-desconto2,2)

print("---------------------------------------------")

total= valorfinal1+valorfinal2
print(f"TOTAL DA COMPRA -> R$ {total}")
