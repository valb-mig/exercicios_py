# FUNÇÃO PARA ADICIONAR LINHAS À TABELA.

def linha(tamanho,texto):
  print('-'*tamanho)
  print(texto)
  print('-'*tamanho)

# CRIAÇÃO DOS TÓPICOS.

print('\n                Bem-Vindo(a) a Pizzaria do Ivalber Miguel')
x =('Código | Descrição  | Pizza Média = M | Pizza Grande = G (30% mais cara)')
tam = len(x)

# TABELA DE INFORMAÇÕES.

linha(tam,x)

print('  21   | Napolitana |        R$ 20,00 |                        R$ 26,00')
print('  22   | Margherita |        R$ 20,00 |                        R$ 26,00')
print('  23   | Calabresa  |        R$ 25,00 |                        R$ 32,50')
print('  24   | Toscana    |        R$ 30,00 |                        R$ 39,00')
print('  25   | Portuguesa |        R$ 30,00 |                        R$ 39,00')

print('-'*tam)


# VALOR TOTAL.

total = 0

# INÍCIO DO LOOP PRINCIPAL.

while True:

  # VERIFICAÇÃO DO TAMANHO DA PIZZA.

  tam_pizza = input('\nEscolha o tamanho da pizza (M ou G): ')
  
  if(tam_pizza != 'M' and tam_pizza != 'G'):
    print('Valor inválido!..')
    continue
    
  # VERIFICAÇÃO DO CÓDIGO DA PIZZA.

  while True:

    id_pizza = int(input('\nQual o código da pizza: '))
    
    if (id_pizza > 25):
      print('Valor inválido...')
      continue
    
    elif (id_pizza < 21):
      print('Valor inválido...')
      continue
    
    else:
      break
  
  # ATRIBUIÇÃO DO SABOR AO CÓDIGO.

  if (id_pizza == 25):
    pizza = 'Portuguesa'
    valor = 30.00
    if (tam_pizza == 'G'):
      valor = 39.00
    print('\n-> Você pediu uma Pizza {}! <-'.format(pizza))
    
  elif (id_pizza == 24):
    pizza = 'Toscana'
    valor = 30.00
    if (tam_pizza == 'G'):
      valor = 39.00
    print('\n-> Você pediu uma Pizza {}! <-'.format(pizza))
    
  elif (id_pizza == 23):
    pizza = 'Calabresa'
    valor = 25.00
    if (tam_pizza == 'G'):
      valor = 32.50
    print('\n-> Você pediu uma Pizza {}! <-'.format(pizza))

  elif (id_pizza == 22):
    pizza = 'Margherita'
    valor = 20.00
    if (tam_pizza == 'G'):
      valor = 26.00
    print('\n-> Você pediu uma Pizza {}! <-'.format(pizza))

  elif (id_pizza == 21):
    pizza = 'Napolitana'
    valor = 20.00
    if (tam_pizza == 'G'):
      valor = 26.00
    print('\n-> Você pediu uma Pizza {}! <-'.format(pizza))

  else:
    print('\nValor inválido!.')
    continue

  # ADICIONAR MAIS ALGO?
  
  outra = int(input('\nDeseja pedir mais algo?\n\n1 - Sim\n0 - Não \n|\n------> '))
  if (outra == 0):
    break
  
  elif (outra == 1):
    total = total + valor
    continue

# FINALIZAÇÃO

print('\nTotal a ser pago: R$ {:.2f}'.format(total+valor))
