#ESTRUTURA  CONDICIONAL IF  ELSE(se senao)  ->  True  or  False (verdadeiro ou  falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

#x=10  

#if x > 1000:
 #   print("verdade")
#else:
 #   print("falso")
 #   print("falso")
 #   print("falso")
 #   print("falso")

#nome = "teste"
#if "testee" != nome:
#    print(1)
#else:
#    print(2)

#exercicios - if Else
#atividade1

#print("**********atividade1**********")

#idade = int(input("digite sua idade: "))

#if idade >= 18:
#    print("voce e maior de idade,")
#else:
#    print("voce e menor de idade,")

#print("**********atividade2**********")

#idade = int(input("digite sua idade: "))
#if idade ==0 or idade > 120:
#    print("idade invalida")
#else:
#    print("valida")

#print("**********atividade3**********")

#email =(input("digite seu email: "))
#senha =(input("digite sua senha: "))

#if "python@senai.com" == email and senha == "12345678" :
#    print("usuario e senha valido")
#else: 
#    print("usuario ou senha invalido")

#atividade 1 "vogal e consoante"

#print("----------------vogal e consoante----------------")
#letra = input("digite uma letra: ").lower()

#if letra == "a" or letra ==  "e" or letra == "i" or letra == "o" or letra == "u"  :
#    print("a letra digitada é uma vogal, ")
#else :
#    print("a letra digitada é uma consoante, ")


#atividade 2 "maior ou menor"

print("----------------maior e menor----------------")

n1 = float(input("digite um numero: "))
n2 = float(input("digite outro numero: "))

if n1 > n2:
    print(f"numero maior:", n1)
    print(f"numero menor:", n2)
else :
    print(f"numero maior:", n2)
    print(f"numero menor:", n1)
