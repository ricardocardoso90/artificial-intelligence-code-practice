# Importando a biblioteca
import pandas as pd

# Verificando a versão do pandas
print("Versão do pandas:", pd.__version__)

# Criando o dicionário com os dados
df_medidas = {
    'idade': [15, 18, 25, 25, 40, 55, 58, 60, 80],
    'altura': [160, 162, 165, 168, 175, 178, 178, 178, 190]
}

# Criando um DataFrame a partir do dicionário
df = pd.DataFrame(df_medidas)

# Exibindo o DataFrame
print("\nDataFrame:")
print(df)
