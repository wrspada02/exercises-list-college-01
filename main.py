""" 1º) Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes """

def exercise01():
  vowels = ['a', 'e', 'i', 'o', 'u']
  inputCharacters = []

  for i in range(10):
    inputCharacters.append(input('Digite um caracter: ').lower()[:1])

  consonants = list(filter(lambda x: x not in vowels, inputCharacters))

  print(f'Consoantes: {consonants}')

""" 2º) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da
média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . .).  """

def exercise02():
  yearTemperature = []
  monthTemperatureHigherThanAverage = {}
  mappedMonthByIndex = {
    '0': 'Janeiro',
    '1': 'Fevereiro',
    '2': 'Março',
    '3': 'Abril',
    '4': 'Maio',
    '5': 'Junho',
    '6': 'Julho',
    '7': 'Agosto',
    '8': 'Setembro',
    '9': 'Outubro',
    '10': 'Novembro',
    '11': 'Dezembro'
  }

  for i in range(12):
    yearTemperature.append(float(input(f'Digite a temperatura média do mês {i+1} em graus celsius: ')))
  
  averageTemperature = sum(yearTemperature) / len(yearTemperature)
  
  for i, temperature in enumerate(yearTemperature):
    if temperature > averageTemperature:
      monthTemperatureHigherThanAverage[i] = temperature
  
  print(f'Temperaturas acima da média anual: ')

  for monthIndex, temperature in monthTemperatureHigherThanAverage.items():
    print(f'{mappedMonthByIndex[str(monthIndex+1)]} - {temperature}°C')

""" 3º) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média
de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
alunos com media maior que 7.0 ---> ", somaAlunos) """

def exercise03():
  studentsAverage = []

  for i in range(10):
    studentNote = 0

    for j in range(4):
      studentNote += float(input(f'Digite a nota {j+1} do aluno {i+1}: '))
    
    studentsAverage.append(studentNote / 4)
  
  print(f'Alunos com média maior ou igual a 7.0: {len(list(filter(lambda x: x >= 7, studentsAverage)))}')
