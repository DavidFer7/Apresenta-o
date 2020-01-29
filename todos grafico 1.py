''' importar bibliotecas'''
import pandas as pd
import matplotlib.pyplot as plt

''' carregar aquivo e atribuir a uma variavel'''
projeto = pd.read_csv('C:/Users/David/Downloads/IaC.csv')

''' filtrar colunas e atribuir a variaveis'''
selcolunas = projeto['Energia']
anocolu = projeto['Ano']

''' criar legendas no topo do grafico'''
plt.ylabel('Valores de consumo')

''' criar abaixo do eixo x do grafico'''
plt.xlabel('Ano e Mês')

'''rotacionar legendas do eixo x'''
plt.xticks(rotation=90)

''' criar grafico'''
plt.plot(anocolu,selcolunas)

''' criar legedas acima do grafico'''
plt.title('Consumo')


''' criar grades no fundo do grafico'''
plt.grid(True)

''' alterar cor no grafico'''
plt.plot(anocolu, selcolunas, color='yellow')

''' mostrar grafico criado'''
plt.show()

