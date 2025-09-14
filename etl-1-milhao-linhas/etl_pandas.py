import pandas as pd

df = pd.read_csv("Projetos\etl-1-milhao-linhas\data\measurements.txt",
                 sep=";",
                 header=None,
                 names=['station', 'measurements']
                )

print(df)

df_agg = df.groupby('station')
df_kpi = df_agg['measure'].agg({
        'min':'min',
        'max':'max',
        'mean':'mean'
    })

# df_sort = df_kpi.sort_values('station')