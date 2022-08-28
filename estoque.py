# FUNÇÃO PARA ADICIONAR LINHAS À TABELA.

def borda(texto,tamanho):
  print('\n+','-'*tamanho,'+')
  print('|',texto,'|')
  print('+','-'*tamanho,'+')

# FUNÇÃO PARA CADASTRAR PRODUTO

def cadastrarProduto(id):
  
  print('\n')
  texto = 'Cadastro de produto'
  tam = len(texto)
  borda(texto,tam)
  
  print('\n -> O id do produto será: 00{} <-'.format(id))
  
  # ADICIONAR NOME

  while True:
    nome = input('\nQual o nome do produto que deseja cadastrar? ')
    
    if(nome == ''):
      print('\n-> Digite o nome do produto! <-')
      continue
    
    # ATRIBUIR NOME
    
    else:
      break
  
  # ADICIONAR FABRICANTE

  while True:
    fabricante = input('\nQual o nome do fabricante do produto? ')
    
    if(fabricante == ''):
        print('\n-> Digite o nome do fabricante! <-')
        continue

    # ATRIBUIR FABRICANTE

    else:
      break
  
  # ADICIONAR VALOR

  while True:
    valor = float(input('\nQual o valor do produto em (R$)? '))

    if(valor < 1.0):
      print('\n-> Não é possível cadastrar um produto abaixo de R$ 1,00 <-')
      continue

    # ATRIBUIR VALOR

    else:
      break
  
  # ADICIONAR À LISTA NO DICIONÁRIO

  produto = {'id':id,'nome':nome,'fabricante':fabricante,'valor':valor}
  lista_prod.append(produto.copy())

# FUNÇÃO PARA CONSULTAR PRODUTO

def consultarProduto():

  print('\n')
  texto = 'Consulta de produto'
  tam = len(texto)
  borda(texto,tam)
  
  print('\nEscolha uma das opções!')
  print('\n1 - Consultar todos os produtos\n2 - Consultar produtos por ID\n3 - Consultar produtos por FABRICANTE\n4 - Voltar')

  while True:
    try:
      opc = int(input('|\n+-------> '))
    
      # CONSULTAR TODOS

      if(opc == 1):
        while True:
          print('\nTodos os produtos cadastrados\n')
          print('-'*27)

          for produto in lista_prod:
            for key, value in produto.items():
              print('{} : {}'.format(key,value)) 
            print('-'*27)
          break

      # CONSULTAR ID

      elif(opc == 2):
        while True:
          entrada = int(input('\nDigite o ID do produto: '))
          print('-'*27)

          for produto in lista_prod:
            if(produto['id'] == entrada):
              for key, value in produto.items():
                print('{} : {}'.format(key,value))   
              print('-'*27)
          break
      
      # CONSULTAR FABRICANTE
      
      elif(opc == 3):
        while True:
          entrada = input('\nDigite o FABRICANTE do produto: ')
          print('-'*27)

          for produto in lista_prod:
            if(produto['fabricante'] == entrada):
              for key, value in produto.items():
                print('{} : {}'.format(key,value))   
              print('-'*27)
          break
      
      # ERROS
      
      else:
        print('\n--> Produto não cadastrado <--')
        break

      x = int(input('\n1 - Retornar\n--> '))
      if(x == 1):
        break
    
    # ERROS

    except ValueError:
      print('\n\n\n---------------> Opção inválida!!! <---------------')
      continue

# FUNÇÃO PARA REMOVER PRODUTO

def removerProduto():
  
  print('\n')
  texto = 'Remover produto'
  tam = len(texto)
  borda(texto,tam)

  codigo = int(input('\nDigite o ID do produto: '))
        
  for produto in lista_prod:
    if(produto['id'] == codigo):
      lista_prod.remove(produto)

# INÍCIO MAIN

texto = 'Seja Bem-Vindo(a) ao Controle de estoque da Mercearia do Ivalber Miguel'
tam = len(texto)
borda(texto,tam)

# PARÂMETROS ACUMULADORS

id = 0

# DICIONÁRIO QUE IRÁ ACUMULAR OS PRODUTOS

lista_prod = []

# MENU

while True:

  texto2 = ('Selecione uma das opções')
  tam2 = len(texto2)
  borda(texto2,tam2)

  print('\n1 - Cadastrar Produto\n2 - Consultar Produto(s)\n3 - Remover Produto\n4 - Sair')
  
  # OPÇÕES

  try:
    opc = int(input('|\n+-------> '))
    
    # CADASTRAR

    if(opc == 1):
      id += 1
      cadastrarProduto(id)
      print('\n\n\n---------------> Produto Cadastrado! <---------------')      
      continue

    # CONSULTAR

    elif(opc == 2):
      consultarProduto()
      continue

    # REMOVER

    elif(opc == 3):
      removerProduto()
      print('\n\n\n---------------> Produto Removido! <---------------')
      continue

    # SAIR

    elif(opc == 4):
      print('\nSaindo...')
      break
    
    # ERROS

    else:
      print('\n\n\n---------------> Essa opção não existe!!! <---------------')
      continue

  except ValueError:
    print('\n\n\n---------------> Opção inválida!!! <---------------')
    continue
