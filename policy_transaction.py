## Step 1: import Python libraries and dataset, perform EDA

# %%

# !pip install rake_nltk
from datetime import datetime

import pandas as pd
import sys
import numpy as np
import warnings
import re

warnings.filterwarnings("ignore")


def removenumber(x):
    sumInsuredT = str(x).split(".")
    sumInsuredT = sumInsuredT[0]
    sumInsuredT = re.sub("[^0-9]", "", sumInsuredT)
    sumInsuredT = re.sub(r'[a-z]+', "", sumInsuredT)
    return sumInsuredT


# df = pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xxeevdialfl7')   # 250 rows × 38 columns
df = pd.read_csv('RecieptOrions.csv')  # same data 250 rows × 38 columns
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
    # result = binder.Query(row['ID'] == 'iIemID')

    # How to Query the panda database
    r = binder[binder.BinderNo == row['BinderNo']]

    createdAt = ""
    createdON = ""
    startAt = ""
    startON = ""
    endAt = ""
    endOn = ""
    sumInsuredT = 0

    print(row['nCreated'])

    createdArr = str(row['nCreated']).replace("nil", "").replace("Null", "").replace("nan","").split()
    # nStartArr = row['nCreated'].split()

    #print(row['nCreated'])

    if len(createdArr) > 0:
        createdAt = createdArr[1]
        createdON = createdArr[0]
        print(row['nCreated'])


    else:
        createdAt = ""
        createdON = ""

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
            sumInsuredT = str(rr['SumInsured']).split(".")

            sumInsuredT = sumInsuredT[0]
            sumInsuredT = re.sub("[^0-9]", "", str(rr['SumInsured']))
            sumInsuredT = re.sub(r'[a-z]+', "", sumInsuredT)

    # print(Premium,sumInsured,policyNumber)
    # sys.exit()

    cleanData.append([
        'Authorized At',
        '',
        row['nDate'].replace(" 00:00:00.000", ""),
        row['Customer'],
        '',
        '',
        '',
        '',
        createdAt,
        '',
        createdON,
        row['Purpose'],
        '',
        '',
        '',
        '',
        row['ReceiptNo'],
        '',
        '',
        removenumber(row['Premium']),
        removenumber(sumInsuredT),
        '',
        '',
        nEnd,
        policyNumber,
        nStart,
        row['Service'],
        removenumber(row['nAmount']),
        '',
        row['Payee'],
        row['Stamp'],
        row['nTime'],
        row['GCT'],
        '',
        row['nRType'],
        '',
        ''
    ])

dataOutput = pd.DataFrame(cleanData, columns=[
    'Authorized At',
    'Authorized by',
    'Authorized On',
    'Billing Account',
    'Branch',
    'Broker Reference ID',
    'Created At',
    'Created By',
    'Created On',
    'Currency',
    'Date of Transaction',
    'Description',
    'Effective Date',
    'Effective Expiry Date',
    'Effective Text',
    'End Time',
    'Endorsement No',
    'FA Excess Description',
    'FA Excess Percent',
    'Gross Premium',
    'Insured',
    'Net Amount Due',
    'Period',
    'Policy End Date',
    'Policy No',
    'Policy Start Date',
    'Service Charge',
    'Source Comm Amount',
    'Source Comm Rate',
    'Source Name',
    'Stamp Duty',
    'Start Time',
    'Tax Amount',
    'Tax Percent',
    'Transaction Type',
    'Risk Items ',
    'Policy Limits of Liability'
])

# displaying the DataFrame
# print('DataFrame:\n', dataOutput)

print("reach")

# saving the DataFrame as a CSV file
gfg_csv_data = dataOutput.to_csv('orion_transaction.tsv', index=False, sep="\t")
gfg_csv_data = dataOutput.to_csv('orion_transaction.csv', index=False)

# print('\nCSV String:\n', gfg_csv_data)

# print(df);

print(len(cleanData))

print("finish")

# print(df);
# %%
