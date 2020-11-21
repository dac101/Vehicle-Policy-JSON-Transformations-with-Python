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
df = pd.read_csv('OrionsClaims.csv')  # same data 250 rows × 38 columns
risk = pd.read_csv('InsurableOrions.csv')  # same data 250 rows × 38 columns
claimsDetail = pd.read_csv('ClaimsDetails.csv')  # same data 250 rows × 38 columns
customers = pd.read_csv('CustomerOrions.csv')  # same data 250 rows × 38 columns
binder = pd.read_csv('PolicyOrions.csv', usecols=[
    'iIemID',
    'PolicyNo',
    'SumInsured',
    'Premium',
    'nStart',
    'nEnd',
    'BinderNo'
])  # same data 250 rows × 38 columns
# create the pandas dataframe

binder = binder.sort_values(by=['iIemID'])

cleanData = []
counter = 0;

for index, row in df.iterrows():
    counter = counter + 1;
    print("row" + str((counter + 1)))

    policyNumber = ""
    sumInsured = 0
    Premium = 0
    nEnd = ''
    nStart = ''
    vehBodyType = ''
    vehCC = ''
    vehChasis = ''
    vehEngine = ''
    vehMake = ''
    vehModel = ''
    vehReg = ''
    vehTonnage = ''
    vehYear = ''
    riskDescription = ''
    riskId = ''
    status = ''
    email = ''

    # result = binder.Query(row['ID'] == 'iIemID')

    # How to Query the panda database
    r = binder[binder.BinderNo == row['NumBinderNo']]
    risk = risk[risk.ID == row['iIemID']]
    claimsDetail = claimsDetail[claimsDetail.ID == row['ID']]
    customer = customers[customers.Id == row['Customer']]
    # print(len(r))
    # sys.exit()

    # Remove null
    df['Customer'].fillna("", inplace=True)

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
            nEnd = rr['nEnd']
            nStart = rr['nStart']

    if len(risk) > 0:
        # print(row['ID'])
        # print(r['iIemID'])
        for i, item in risk.iterrows():
            vehBodyType = item['BodyType']
            vehCC = item['CC']
            vehChasis = item['Chassis']
            vehEngine = item['Engine']
            vehMake = item['Make']
            vehModel = item['Model']
            vehReg = item['Reg']
            vehTonnage = item['Tonnage']
            vehYear = item['Year']
            riskDescription = item['Particular']
            riskId = item['ID']

    if len(claimsDetail) > 0:
        # print(row['ID'])
        # print(r['iIemID'])
        for i, item in claimsDetail.iterrows():
            status = item['Status']

    if len(customer) > 0:
        # print(row['ID'])
        # print(r['iIemID'])
        for i, item in customer.iterrows():
            email = item['Email']

    # print(Premium,sumInsured,policyNumber)
    # sys.exit()

    CurrentBI = ''
    CurrentOD = ''
    CurrentPD = ''

    # Third Party  # Contributory   # In    # N / A   # Client   # Dispute

    if row['Liability'] == 'Third Party':
        CurrentPD = row['CostDamage']
    if row['Liability'] == 'Client':
        CurrentOD = row['CostDamage']
    if row['Liability'] == 'Client':
        CurrentPD = row['CostDamage']
    if row['Liability'] == 'Contributory':
        CurrentBI = row['CostDamage']

    settle = False
    if row['Settle'] == 'Y':
        settle = True
    cleanData.append([
        row['ID'],
        row['PolicyNo'],
        row['NatureOfDamage'],
        row['TPSettleAmount'],
        row['Reserve'],
        row['OwnAmount'],
        row["TPRecSettleAmount"]
    ])

dataOutput = pd.DataFrame(cleanData, columns=[
    'Claim ID',

    "Insurer Policy Number",
    "Nature Of Damage",
    "TPSettleAmount",
    "Reserve",
    "OwnAmount",
    "TPRecSettleAmount",
])

# displaying the DataFrame
# print('DataFrame:\n', dataOutput)

print("reach")

# saving the DataFrame as a CSV file
gfg_csv_data = dataOutput.to_csv('notes_claims.tsv', index=False, sep="\t")
gfg_csv_data = dataOutput.to_csv('notes_claims.csv', index=False)

# print('\nCSV String:\n', gfg_csv_data)

# print(df);

print(len(cleanData))

print("finish")

# print(df);
# %%
