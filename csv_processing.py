#%% Output parser
import json, re, os

import pandas as pd
from pandas import DataFrame

filepath = "data/dementia_dbs_v1_output.csv"
df = pd.read_csv(filepath)

row1 = df.iloc[0]
row1_stmts = json.loads(row1["Statements"])
cols = [l[0] for l in row1_stmts]

errors = []

for ind, row in df.iterrows():
    stmts_str = row["Statements"]
    print(ind, row["Title"])
    if isinstance(stmts_str, str):
        try:
            stmts = json.loads(stmts_str)        
            for i, col in enumerate(cols):
                df.at[ind, col] = stmts[i][1] # Take second item of each list 
        except:
            errors.append([ind, row])
new_filepath = F"{os.path.splitext(filepath)[0]}_annot.csv"
df.to_csv(new_filepath)