import pandas as pd

pd.set_option("display.max_column", None)

df = pd.read_csv("japan_birth.csv", sep=',')

print(df)