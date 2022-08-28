menu = 'Menu de feijoada'
tam = len(menu)

# FUNÇÃO PARA ADICIONAR LINHAS À TABELA.

def borda(texto,tamanho):
  print('\n+','-'*tamanho,'+')
  print('|',texto,'|')
  print('+','-'*tamanho,'+')

# FUNÇÃO PARA DETERMINAR A QUANTIDADE DA FEIJOADA.

def volumeFeijoada():
  volume = 0
  
  while True:
    try:
      ml = int(input('\nDigite a quantidade (em ml): '))

      if(ml < 300):
        print('\n-->Valor abaixo do permitido (min 300ml | max 5l)<--')
        continue
        
      elif(ml > 5000):
        print('\n-->Valor acima do permitido (min 300ml | max 5l)<--')
        continue
        
      else:
        volume = ml * 0.08
        return volume
        break

    except ValueError:
      print('Você digitou um valor não numérico, Tente novamente')
      continue

# FUNÇÃO PARA DEFINIR O VALOR DAS OPÇÕES.

def opcaoFeijoada():

  texto = 'Escolha a opção da feijoada.'
  tam = len(texto)
  borda(texto,tam)

  print('\n-> b - Básica (Feijão + Paiol + Costelinha)')
  print('\n-> p - Premium (Feijão + Paiol + Costelinha + Partes de porco)')
  print('\n-> s - Suprema (Feijão + Paiol + Costelinha + Partes de porco + Charque + Calabresa + Bacon)')

  opcao = 0

  while True:
    
    opc = input('|\nQual a opção: ')
      
    if(opc == 'b'):
      opcao = 1.00
      return opcao
      break
      
    elif(opc == 'p'):
      opcao = 1.25
      return opcao
      break
      
    elif(opc == 's'):
      opcao = 1.50
      return opcao
      break
      
    else:
      print('|\n-->Valor Inválido<--')
      continue

# FUNÇÃO PARA ADICIONAR ACOMPANHAMENTOS

def acompanhamentoFeijoada():

  texto = 'Adicionar acompanhamentos'
  tam = len(texto)
  borda(texto,tam)

  print ('\n0 - Finalizar pedido\n1 - 200g de arroz\n2 - 150g de farofa\n3 - 100g de couve cozida\n4 - 1 Laranja descascada')
  
  # DECLARAÇÃO DA VARIÁVEL DE ACÚMULO.

  sub = 0

  while True:
    
    opc = int(input('|\nQual a opção: '))

    if(opc == 0):
      return sub
      break

    elif(opc == 1):
      add = 5.00
      sub = add + sub
      continue

    elif(opc == 2):
      add = 6.00
      sub = add + sub
      continue

    elif(opc == 3):
      add = 7.00
      sub = add + sub
      continue
      
    elif(opc == 4):
      add = 3.00
      sub = add + sub
      continue

    else:
      print('|\n-->Valor Inválido<--')
      continue

# INÍCIO

print('\nBem vindo(a) ao programa de feijoada do Ivalber Miguel')
borda(menu,tam)


volume = volumeFeijoada()
opcao = opcaoFeijoada()
adicional = acompanhamentoFeijoada()

total = (volume * opcao) + adicional

print('\n-->O valor a ser pago é (R$ {:.2f}) (volume = {:.2f} * opção = {:.2f} + acompanhamentos = {:.2f})<--\n'.format(total,volume,opcao,adicional))

