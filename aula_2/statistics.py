import pandas as pd

dict_medidas = {
  'idade': [15, 18, 25, 25, 40, 55, 58, 60, 80],
  'alura': [160, 162, 165, 168, 175, 178, 178, 178, 190],
}

print(dict_medidas)

df_medidas = pd.DataFrame.from_dict(dict_medidas)
# print(df_medidas)

media = df_medidas.idade.mean()

print(media)