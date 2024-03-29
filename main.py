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

""" 4º) Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
armazenado). Após esta entrada de dados, faça:
1. Mostre a quantidade de valores que foram lidos;
2. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
3. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
4. Calcule e mostre a soma dos valores;
5. Calcule e mostre a média dos valores;  """

def exercise04():
  numbers = []
  currentNumber = 0

  while currentNumber != -1:
    currentNumber = int(input('Digite um número: '))
    if currentNumber != -1:
      numbers.append(currentNumber)
  
  print(f'Quantidade de valores lidos: {len(numbers)}')
  print(f'Valores informados: {numbers}')
  print(f'Valores inversos: {numbers[::-1]}')
  print(f'Soma dos valores: {sum(numbers)}')
  print(f'Média dos valores: {sum(numbers) / len(numbers)}')

""" 5º) Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do
atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que
receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do
atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m """

def exercise05():
  athletes = {}
  currentAthlete = 'Patati Patatá'

  while currentAthlete != '':
    currentAthlete = input('Digite o nome do atleta: ')
    if currentAthlete != '':
      jumps = []

      for i in range(5):
        jumps.append(float(input(f'Digite a distância do salto {i+1} em metros: ')))

      athletes[currentAthlete] = jumps

  for athlete, jumps in athletes.items():
    print(f'Atleta: {athlete}')
    for i, jump in enumerate(jumps):
      print(f'Salto {i+1}: {jump}m')
    print(f'Média dos saltos: {sum(jumps) / len(jumps)}m')

""" 6º) Foram anotadas as idades e alturas de 7 alunos. Faça um Programa que determine quantos alunos
com mais de 13 anos possuem altura inferior à média de altura desses alunos.
idades = [14, 12, 13, 16, 18, 20, 13]
alturas = [1.8, 1.9, 1.0, 2.0, 1.4, 1.3, 1.85] """

def exercise06():
  ages = [14, 12, 13, 16, 18, 20, 13]
  heights = [1.8, 1.9, 1.0, 2.0, 1.4, 1.3, 1.85]
  averageHeight = sum(heights) / len(heights)
  studentsWithMoreThan13YearsOldAndHeightLessThanAverage = 0

  for i in range(len(ages)):
    if ages[i] > 13 and heights[i] < averageHeight:
      studentsWithMoreThan13YearsOldAndHeightLessThanAverage += 1

  print(f'Alunos com mais de 13 anos e altura inferior à média: {studentsWithMoreThan13YearsOldAndHeightLessThanAverage}')

exercise06()
