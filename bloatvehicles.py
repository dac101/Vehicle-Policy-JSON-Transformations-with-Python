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
df = pd.read_csv('InsurableBoatNoMotorOrions.csv')  # same data 250 rows × 38 columns
binder = pd.read_csv('PolicyOrions.csv', usecols=[
    'iIemID',
    'PolicyNo',
    'SumInsured',
    'Premium',
])  # same data 250 rows × 38 columns
# create the pandas dataframe

binder = binder.sort_values(by=['iIemID'])

cleanData = []
counter = 0;

for index, row in df.iterrows():
    counter = counter+1;
    print("row"+str((counter+1)))

    policyNumber = ""
    sumInsured = 0
    Premium = 0
    # result = binder.Query(row['ID'] == 'iIemID')

    # How to Query the panda database
    r = binder[binder.iIemID == row['ID']]

    # print(len(r))
    # sys.exit()

    # Remove null
    df['Mort'].fillna("", inplace=True)
    df['ID'].fillna("", inplace=True)
    df['Particular'].fillna("", inplace=True)
    df['BodyType'].fillna("", inplace=True)
    df['CC'].fillna("", inplace=True)
    df['Chassis'].fillna("", inplace=True)
    df['Engine'].fillna("", inplace=True)
    df['Make'].fillna("", inplace=True)
    df['Model'].fillna("", inplace=True)
    df['Reg'].fillna("", inplace=True)
    df['Tonnage'].fillna("", inplace=True)
    df['Year'].fillna("", inplace=True)


    if len(r) > 0:
        # print(row['ID'])
        # print(r['iIemID'])
        for i, rr in r.iterrows():
            r['PolicyNo'].fillna("", inplace=True)
            r['SumInsured'].fillna("", inplace=True)
            r['Premium'].fillna("", inplace=True)

            policyNumber = rr['PolicyNo']
            sumInsured = rr['SumInsured']
            Premium = rr['Premium']
       # print(Premium,sumInsured,policyNumber)
        #sys.exit()

    cleanData.append([
        row['nDate'],
        '',
        '',
        '',
        '',
        '',
        '',
        ' ',
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
        '',
        sumInsured,
        '',
        '',
        row['BodyType'],
        row['CC'],
        '',
        row['Reg'],
        '',
        '',
        row['Tonnage'],
        row['Engine'],
        ''
    ])

dataOutput = pd.DataFrame(cleanData, columns=[
    'Date First Effected',
    'Deleted By',
    'Deleted On',
    'Excess Amount',
    'Excess Conditions',
    'Excess Maximum Limit',
    'Excess Minimum Limit',
    'Excess Percent',
    'Is Deleted',
    'Is Vehicle in Disrepair',
    'Is Vehicle Modified',
    'Item Position',
    'Mortgagee Text',
    'Policy No',
    'Premium',
    'Registered Owner',
    'Risk Item No',
    'Risk Item Type',
    'Section Number',
    'Sum Insured',
    'Sum Insured Type',
    'Usage Code',
    'MH Body Type',
    'MH Veh CC Rating',
    'MH Reg Location',
    'MH Reg No',
    'MH Passesger Capacity',
    'MH Hull No',
    'MH Tonnage',
    'MH Engine No',
    'MH Authorized Operator'
])

# displaying the DataFrame
# print('DataFrame:\n', dataOutput)

print("reach")

# saving the DataFrame as a CSV file
gfg_csv_data = dataOutput.to_csv('orions_risk_items_marine_vessel_vehicles.tsv', index=False, sep="\t")
gfg_csv_data = dataOutput.to_csv('orions_risk_items_marine_vessel_vehicles.csv', index=False)

# print('\nCSV String:\n', gfg_csv_data)

# print(df);

print(len(cleanData))

print("finish")

# print(df);
# %%
