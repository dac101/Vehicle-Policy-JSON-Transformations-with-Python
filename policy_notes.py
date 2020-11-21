## Step 1: import Python libraries and dataset, perform EDA

# %%

# !pip install rake_nltk
from datetime import datetime

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# df = pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xalfl7')   # 250 rows × 38 columns
df = pd.read_csv('PolicyOrions.csv')  # same data 250 rows × 38 columnsxeevdi
# create the pandas dataframe

cleandData = []

for index, row in df.iterrows():
    cleandData.append([
        row['Customer'],
        row['PolicyNo'],

        row['nRate'],
        row['Particular'],
        row['ScopeOfCover'],
        row['Comments'],
    ])

dataOutput = pd.DataFrame(cleandData, columns=[
    'Account Code',
    'Policy No',

    'nrate',
    'Particular',
    'ScopeOFCover',
    'Comments',

])

# displaying the DataFrame
# print('DataFrame:\n', dataOutput)

# saving the DataFrame as a CSV file
gfg_csv_data = dataOutput.to_csv('notes_policy.tsv', index=False, sep="\t")
gfg_csv_data = dataOutput.to_csv('notes_policy.csv', index=False)

# print('\nCSV String:\n', gfg_csv_data)

# print(df);

print(len(cleandData));

# print(df);
# %%
