"""2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de
informar a quantidade de vezes em que ela ocorre.
IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
"""

palavra = input("Digite uma Palavra: ")
contar_a = palavra.lower().count('a')

if contar_a > 0:
    print(f"A letra 'a' aparece {contar_a} vezes na string.")
else:
    print("A letra 'a' não está presente na string.")
