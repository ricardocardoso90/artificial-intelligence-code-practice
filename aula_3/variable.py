import pandas as pd

print("Versão do pandas:", pd.__version__)

df_medidas = {
    'idade': [15, 18, 25, 25, 40, 55, 58, 60, 80],
    'altura': [160, 162, 165, 168, 175, 178, 178, 178, 190]
}

df = pd.DataFrame(df_medidas)

print("\nDataFrame:")
print(df)
