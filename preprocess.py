import pandas as pd

data = pd.read_csv('dataset.csv')

data = data.drop_duplicates(['content'],keep='first')

data.to_csv('dataset.csv')