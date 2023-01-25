#%%
import os

import pandas as pd

DF_PATH = "data/obesity_eating_v1_covidence.csv"
DF_ROOT = os.path.splitext(DF_PATH)[0]

df = pd.read_csv(DF_PATH)

#%%
df["Review"] = df["Tags"].str.contains("rev")
df["Anorexia"] = df["Tags"].str.contains("anorexia")
df["Obesity"] = df["Tags"].str.contains("obesity")
df["Non_specific"] = df["Tags"].str.contains("non_specific")
df["Case or non_outcome"] = df["Tags"].str.contains("non_outcome|case_report")

#%%

df.to_csv(F"{DF_ROOT}_annot.csv")

#%% Overall

df_sub = df

n_total = len(df_sub)
n_specific = len(df_sub.loc[(df_sub["Non_specific"] == False)])
n_primary = len(df_sub.loc[(df_sub["Review"] == False) & (df_sub["Case or non_outcome"] == False)])

print(F"Total: {n_total} | Specific: {n_specific} | Primary: {n_primary}\n{n_primary / n_total * 100}% | {n_primary / n_specific * 100}%")


#%% Anorexia
df_sub = df.loc[df["Anorexia"]]

n_total = len(df_sub)
n_specific = len(df_sub.loc[(df_sub["Non_specific"] == False)])
n_primary = len(df_sub.loc[(df_sub["Review"] == False) & (df_sub["Case or non_outcome"] == False)])

print(F"Total: {n_total} | Specific: {n_specific} | Primary: {n_primary}\n{n_primary / n_total * 100}% | {n_primary / n_specific * 100}%")

#%% Obesity
df_sub = df.loc[df["Obesity"]]

n_total = len(df_sub)
n_specific = len(df_sub.loc[(df_sub["Non_specific"] == False)])
n_primary = len(df_sub.loc[(df_sub["Review"] == False) & (df_sub["Case or non_outcome"] == False)])

print(F"Total: {n_total} | Specific: {n_specific} | Primary: {n_primary}\n{n_primary / n_total * 100}% | {n_primary / n_specific * 100}%")
