## Step 1: import Python libraries and dataset, perform EDA

# %%

# !pip install rake_nltk
from datetime import datetime

import pandas as pd
import sys
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# df = pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xxeevdialfl7')   # 250 rows × 38 columns
df = pd.read_csv('InsurableNoMotorOrions.csv')  # same data 250 rows × 38 columns
binder = pd.read_csv('PolicyOrions.csv', usecols=[
    'iIemID',
    'PolicyNo',
    'SumInsured',
    'Premium',
])  # same data 250 rows × 38 columns
# create the pandas dataframe

binder = binder.sort_values(by=['iIemID'])

cleanData = []

#Remove null
df['Mort'].fillna("", inplace=True)
df['ID'].fillna("", inplace=True)
df['Particular'].fillna("", inplace=True)



counter = 0;

for index, row in df.iterrows():
    counter = counter + 1;
    print("row" + str((counter + 1)))

    policyNumber = ""
    sumInsured = 0
    Premium = 0
    # result = binder.Query(row['ID'] == 'iIemID')

    # How to Query the panda database
    r = binder[binder.iIemID == row['ID']]

    # print(len(r))
    # sys.exit()

    if len(r) > 0:

        r['PolicyNo'].fillna("", inplace=True)
        r['SumInsured'].fillna("", inplace=True)
        r['Premium'].fillna("", inplace=True)

        # print(row['ID'])
        # print(r['iIemID'])
        for i, rr in r.iterrows():
            policyNumber = rr['PolicyNo']
            sumInsured = rr['SumInsured']
            Premium = rr['Premium']
    # print(Premium,sumInsured,policyNumber)
    # sys.exit()

    cleanData.append([
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        row['Mort'],
        policyNumber,
        Premium,
        '',
        row['ID'],
        '',
        row['Particular'],
        sumInsured,
        '',
        ''
    ])

dataOutput = pd.DataFrame(cleanData, columns=[
    'Date First Effected',
    'Deleted By',
    'Deleted On',
    'Exposure Declared Description',
    'Exposure or Declared Value',
    'FA Building Year Built',
    'FA Construction Class',
    'FA Construction of Roof',
    'FA Construction of Wall',
    'FA Height in Storeys',
    'FA Location No',
    'FA Occupancy',
    'FA Occupancy Class',
    'Item Position',
    'Is Deleted',
    'Is Key Location',
    'Mortgagee Text',
    'Policy No',
    'Premium',
    'Registered Owner',
    'Risk Item No',
    'Risk Item Type',
    'Short Description',
    'Sum Insured',
    'Sum Insured Type',
    'Usage Code'
])

# displaying the DataFrame
# print('DataFrame:\n', dataOutput)

print("reach")

# saving the DataFrame as a CSV file
gfg_csv_data = dataOutput.to_csv('orions_non_motor_vehicles.tsv', index=False, sep="\t")
gfg_csv_data = dataOutput.to_csv('orions_non_motor_vehicles.csv', index=False)

# print('\nCSV String:\n', gfg_csv_data)

# print(df);

print(len(cleanData))

print("finish")

# print(df);
# %%
