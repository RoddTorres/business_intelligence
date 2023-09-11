import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# dataAnova = pd.read_csv('Teste.csv', encoding='ISO-8859-1')
dataAnova = pd.read_csv('Teste5.csv')

# print(dataAnova.head())

# modelo = ols('QDE_VENDIDA ~ DESCRICAO * COR * TECIDO', data=dataAnova).fit()

# Para arquivo Teste4.csv
# modelo = ols('QDE_VENDIDA ~ COR * TECIDO * BASE', data=dataAnova).fit()


modelo = ols('QDE_VENDIDA ~ TECIDO * COR', data=dataAnova).fit()

tabela_anova = anova_lm(modelo)

print(tabela_anova)
