''' importar bibliotecas'''
import pandas as pd
import matplotlib.pyplot as plt

''' importar arquivos'''
projeto = pd.read_csv('C:/Users/David/OneDrive/Documentos/codigos python/IaC.csv')

''' selecionar atraves de nome da coluna'''
energia = projeto['Energia']

'''criar boxplot'''
plt.boxplot(energia)

''' criar legendas'''
plt.title('Consumo')

'''criar legendas no eixo y do grafico'''
plt.ylabel('Valores de consumo')

''' criar legenda no eixo x do grafico'''
plt.xlabel('Ano e Mês')

'''acrescentando grid'''
plt.grid(True)

''' mostrar grafico criado'''
plt.show()
