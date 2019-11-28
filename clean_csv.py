import pandas as pd
import os

# Specify directory
path = 'fire_data'
for root,dirs,files in os.walk(path):
    df_all = pd.DataFrame()
    # Find files in directory
    for file in files:
        if file.endswith(".csv"):
            # Delimit files and get rid of tweets with semicolons
            df=pd.read_csv(path + '/' + file, delimiter = ';', error_bad_lines = False)
            # Append fire name to new column
            df['fire'] = file.split('.csv',1)[0]
            df_all = df_all.append(df)
# Send to csv
df_all.to_csv('all_fires.tsv', sep = '\t')
