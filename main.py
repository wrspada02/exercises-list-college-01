# 1º) Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes

def exercise01():
  vowels = ['a', 'e', 'i', 'o', 'u']
  inputCharacters = []

  for i in range(10):
    inputCharacters.append(input('Digite um caracter: ').lower()[:1])

  consonants = list(filter(lambda x: x not in vowels, inputCharacters))

  print(f'Consoantes: {consonants}')

exercise01()
