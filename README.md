## 📖 Sobre.
<p>São apenas alguns exercícios em python requisitados pela faculdade.</p>

<br>


## ⏺ Exercicío - 1
<h3>Objetivo</h3>
 Calcular o desconto de um produto.

- Código

<ul>
  <li>

  ```#=== FUNÇÃO PARA ADICIONAR BORDAS AO TEXTO ===#

  def borda(texto,tamanho):
    print('\n+','-'*tamanho,'+')
    print('|',texto,'|')
    print('+','-'*tamanho,'+')

  # Texto

  txt = 'Bem vindo(a) a loja do Ivalber Miguel'
  tam = len(txt)
  borda(txt,tam)

  #=== ENTRADAS ===#

  valor = float(input('Digite o valor do produto: ')) 
  quant = float(input('|\nDigite a quantidade do produto: '))

  # Condicionais

  if(quant >= 100):
    desc = 10.0
    print('|\nValor sem desconto: {}R$'.format(valor*quant))
    valor = valor * quant
    desc = (desc * valor)/100
    valor = valor - desc
    print('Valor com desconto: {}R$ (desconto de 10%)\n'.format(valor))

  elif(quant >= 20):
    desc = 6.0
    print('|\nValor sem desconto: {}R$'.format(valor*quant))
    valor = valor * quant
    desc = (desc * valor)/100
    valor = valor - desc
    print('Valor com desconto: {}R$ (desconto de 6%)\n'.format(valor))

  elif(quant > 4):
    desc = 3.0
    print('|\nValor sem desconto: {}R$'.format(valor*quant))
    valor = valor * quant
    desc = (desc * valor)/100
    valor = valor - desc
    print('Valor com desconto: {}R$ (desconto de 3%)\n'.format(valor))

  else:
    desc = 0
    print('|\nValor sem desconto: {}R$'.format(valor*quant))
    valor = valor * quant
    desc = (desc * valor)/100
    valor = valor - desc
    print('Valor com desconto: {}R$ (desconto de 0%)\n'.format(valor))

  ```
 
  </li>
</ul>