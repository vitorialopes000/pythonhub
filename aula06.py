#import os
#os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ALIF)
#  SWITCH CASE =>  (mach case) escolha caso (a partir da versão 3.10) 
#match valor
#   case valor

# linguagem = 100

# match linguagem:

#     case "python":
#         print(" é facil")
#     case "java" :
#         print(" muito codigo , python faz com linhas menores")
#     case "c#" :
#         print(" massa")
#     case "js" :
#         print(" sou do back")    
#     case "html" :
#         print(" kauan nao dorme")
#     case 10 :
#         print(" entrou aqui !")
#     case _ :
#         print(" putro caso")

# print("----dias da semana----")
# print("1-segunda")        
# print("2-terça") 
# print("3-quarta") 
# print("4-quinta") 
# print("5-sexta") 
# print("6-sabado") 
# print("7-domingo") 
# print("---------------------------------")
# semana= float(input("digite o numero do dia da semana: "))
# match semana: 
#     case 1:
#         print("segunda")
#     case 2:
#         print("terça")
#     case 3:
#         print("quarta")
#     case 4:
#         print("quinta")
#     case 5:
#         print("sexta")
#     case 6:
#         print("sabado")
#     case 7:
#         print("domingo")
 
# print ("-----𝓂𝓊𝓃𝒹𝑜 𝒹𝑜 𝒸𝑒𝓁𝓊𝓁𝒶𝓇-----")

# print("""
# 1- IPHONE 15 - R$5000,00
# 2- XIAOMI REDNI 13 PRO PLUS 512GB - 2500,00
# 3- SANSUNG S25 265GB - 6999,99
# FRETE: SP-> 10,00
#        MG-> 15,00
#        RS-> 20,00
# """)
# celular= float(input("digite o numero do produto: "))
# valor = 0
# frete = 0
# match celular:
#     case 1:
#         print("IPHONE 15")
#         valor = 5000.00
#     case 2:
#         print("XIAOMI REDMI 13 PRO PLUS 512GB")
#         valor = 2500.00
#     case 3:
#         print("SANSUNG S25 265GB")
#         valor = 6999.99
# estado= (input("digite a sigla do estado: ")) 

# match estado:
#     case "SP":
#         print("10.00 REAIS")
#         frete = 10.00
#     case "MG":
#         print("15.00 REAIS")
#         frete = 15.00
#     case "RS":
#         print("20.00 REAIS")
#         frete = 20.00

# total = valor + frete
# print("*****************************************")
# print(f"VALOR DO CELULAR R$: {valor}")
# print(f"VALOR DO FRETE:  {frete}")
# print(f"VALOR FINAL: {total}")

# import random

# valor = 0
# randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")



#JOGO PEDRA PAPEL E TESOURA

import random

print("******JOGO PEDRA, PAPEL E TESOURA******")

jogo= (input("DIGITE PEDRA, PAPEL OU TESOURA: "))
print("-------------------------------------------")
valor = 0
valor = random.randint(1,3)
papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
print("VOCE")
match jogo:
    case _ if jogo == "papel" : 
        print(f"{papel}")
        jg= 1
    case _ if jogo == "pedra" : 
        print(f"{pedra}")
        jg= 2
    case _ if jogo == "tesoura" : 
        print(f"{tesoura}")
        jg= 3
print("MAQUINA")
match valor:
    case _ if valor == 1 : 
        print(f"{papel}")
    case _ if valor == 2:
        print(f"{pedra}")
    case _ if valor == 3:
        print(f"{tesoura}")


match jg: 
    case _ if jg == 1 and valor == 1:
        print("DEU EMPATE")
    case _ if jg == 1 and valor == 2:
        print("VOCE VENCEU")
    case _ if jg == 1 and valor == 3:
        print("VOCE PERDEU")
    case _ if jg == 2 and valor == 2:
        print("DEU EMPATE")
    case _ if jg == 2 and valor == 1:
        print("VOCE PERDEU")
    case _ if jg == 2 and valor == 3:
        print("VOCE VENCEU")
    case _ if jg == 3 and valor == 3:
        print("DEU EMPATE")
    case _ if jg == 3 and valor == 1:
        print("VOCE VENCEU")
    case _ if jg == 3 and valor == 2:
        print("VOCE PERDEU")

