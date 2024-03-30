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

""" 7º) Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a uma grande
quantidade de organizações:
"Qual o seu voto para prefeito da cidade de São Paulo neste ano?"
As possíveis respostas são:
1- Ricardo Nunes (MDB)
2- Guilherme Boulos (PSOL)
3- Tabata Amaral (PSB)
4- Kim Kataguiri (UNIÃO)
5- Maria Helena (NOVO)
6- Altino Prazeres (PSTU)
0- Sair
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe
ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0,
que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o
programa (1 a 6). Os valores referentes a cada uma das opções devem ser armazenados numa
lista. Após os dados terem sido completamente informados, o programa deverá calcular a
percentual de cada um dos concorrentes e informar o vencedor da enquete. O exemplo do
formato da saída foi informado pela empresa, que é o seguinte:
Candidato Votos %
------------------- ----- ---
Ricardo Nunes 150 2%
Guilherme Boulos 3000 34%
Tabata Amaral 500 5%
Kim Kataguiri 150 2%
Maria Helena 3500 40%
Altino Prazeres 1500 17%
------------------- -------
Total 8800 100%
O candidato mais votado foi Maria Helena, com 3500 votos, correspondendo a 40% dos votos. """


def exercise07():
  def calcPercentage(value, total):
    return value / total * 100
  
  candidates = [0, 0, 0, 0, 0, 0]
  option = True

  while option != 0:
    print('1- Ricardo Nunes (MDB)')
    print('2- Guilherme Boulos (PSOL)')
    print('3- Tabata Amaral (PSB)')
    print('4- Kim Kataguiri (UNIÃO)')
    print('5- Maria Helena (NOVO)')
    print('6- Altino Prazeres (PSTU)')
    print('0- Sair')

    option = int(input("Insira uma opcao: "))

    if option != 0:
      if option == 1:
        candidates[0] += 1
      elif option == 2:
        candidates[1] += 1
      elif option == 3:
        candidates[2] += 1
      elif option == 4:
        candidates[3] += 1
      elif option == 5:
        candidates[4] += 1
      elif option == 6:
        candidates[5] += 1
      else:
        print('Opção inválida! Tente novamente')
  else:
    print('Candidato Votos %')
    print('------------------- ----- ---')
    print(f'Ricardo Nunes {candidates[0]} {calcPercentage(candidates[0], sum(candidates))}%')
    print(f'Guilherme Boulos {candidates[1]} {calcPercentage(candidates[1], sum(candidates))}%')
    print(f'Tabata Amaral {candidates[2]} {calcPercentage(candidates[2], sum(candidates))}%')
    print(f'Kim Kataguiri {candidates[3]} {calcPercentage(candidates[3], sum(candidates))}%')
    print(f'Maria Helena {candidates[4]} {calcPercentage(candidates[4], sum(candidates))}%')
    print(f'Altino Prazeres {candidates[5]} {calcPercentage(candidates[5], sum(candidates))}%')
    print('------------------- -------')
    print(f'Total {sum(candidates)} 100%')

    print(f'O candidatos mais votado foi {candidates.index(max(candidates)) + 1} com {max(candidates)} votos, correspondendo a {calcPercentage(max(candidates),sum(candidates))}% dos votos.')

""" 8º) Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base
em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela
semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200
mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando uma lista de
contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de
valores:
a. $200 - $299
b. $300 - $399
c. $400 - $499
d. $500 - $599
e. $600 - $699
f. $700 - $799
g. $800 - $899
h. $900 - $999
i. $1000 em diante """

def exercise08():
  def calcSalary(sales):
    return 200 + (sales * 0.09)

  sales = [3000, 5000, 7000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
  salaries = []

  for sale in sales:
    salaries.append(calcSalary(sale))
  
  salaryRanges = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0
  }

  for salary in salaries:
    if salary >= 200 and salary <= 299:
      salaryRanges['a'] += 1
    elif salary >= 300 and salary <= 399:
      salaryRanges['b'] += 1
    elif salary >= 400 and salary <= 499:
      salaryRanges['c'] += 1
    elif salary >= 500 and salary <= 599:
      salaryRanges['d'] += 1
    elif salary >= 600 and salary <= 699:
      salaryRanges['e'] += 1
    elif salary >= 700 and salary <= 799:
      salaryRanges['f'] += 1
    elif salary >= 800 and salary <= 899:
      salaryRanges['g'] += 1
    elif salary >= 900 and salary <= 999:
      salaryRanges['h'] += 1
    elif salary >= 1000:
      salaryRanges['i'] += 1

  for key, value in salaryRanges.items():
    print(f'{key}: {value}')
