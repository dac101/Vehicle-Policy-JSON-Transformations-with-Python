## Step 1: import Python libraries and dataset, perform EDA

# %%

# !pip install rake_nltk
from datetime import datetime

import pandas as pd
import numpy as np
import re
import warnings

from numpy.core.defchararray import lower

warnings.filterwarnings("ignore")

def removelettes(x):
    sumInsuredT = str(x).split(".")
    sumInsuredT = sumInsuredT[0]
    print(sumInsuredT)
    sumInsuredT = re.sub("[^0-9]", "", sumInsuredT)
    sumInsuredT = re.sub(r'[a-z]+', "", sumInsuredT)
    print(sumInsuredT)
    return sumInsuredT

# df = pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xalfl7')   # 250 rows × 38 columns
df = pd.read_csv('PolicyOrions.csv')  # same data 250 rows × 38 columnsxeevdi
# create the pandas dataframe

cleandData = []

df.fillna("", inplace=True)

for index, row in df.iterrows():

    createdAt = ""
    createdON = ""
    startAt = ""
    startON = ""
    endAt = ""
    endOn = ""


    createdArr = row['nCreated'].split()
    nStartArr = row['nCreated'].split()
    endArr = row['nEnd'].split()

    if len(createdArr) > 0:
        createdAt = createdArr[1]
        createdON = createdArr[0]

    if len(nStartArr) > 0:
        startAt = nStartArr[0]
        startON = nStartArr[1]


    if len(endArr) > 0:
        endAt = endArr[0]
        #print(row['nEnd'])
       # endOn = endArr[1]


   #Removing all non-numeric characters from string in Python    re.sub("[^0-9]", "", "sdkjh987978asd098as0980a98sd")
    #print(re.sub("[^0-9]", "", row['SumInsured']))
    #re.sub("[^0-9]", "", row['Premium'])

    branch = lower(str(row['BinderNo'])[0:4])

    if    "kin" in str(lower(str(row['BinderNo'])[0:5])):
        branch = "Kingston"
    if   "por" in str(lower(str(row['BinderNo'])[0:5])) :
        branch = "Port Antonio"
    if    "fal" in str(lower(str(row['BinderNo'])[0:5])):
        branch = "Falmouth"
    if    "old" in str(lower(str(row['BinderNo'])[0:5])):
        branch = "Old Harbour"
    if    "och" in str(lower(str(row['BinderNo'])[0:5])):
        branch = "Ocho Rios"
    if   "con" in str(lower(str(row['BinderNo'])[0:5]) ):
        branch = "Constant Spring Road"
    if  "spa" in str(lower(str(row['BinderNo'])[0:5]) ):
        branch = "Spanish Town"
    if   "mor" in str(lower(str(row['BinderNo'])[0:5])) :
        branch = "Morant Bay"
    if    "sov" in str(lower(str(row['BinderNo'])[0:5])):
        branch = "Sovereign"
    if  "lin" in str(lower(str(row['BinderNo'])[0:5])) :
        branch = "Linstead"
    if   "sav" in str(lower(str(row['BinderNo'])[0:5])):
        branch = "Savanna-La-Mar"
    if    "man" in str(lower(str(row['BinderNo'])[0:5])):
        branch = "Mandeville"
    if  "mon" in str(lower(str(row['BinderNo'])[0:5])):
        branch = "Montego Bay"

    if branch == "0":
        branch = ""

    cleandData.append([
        row['Customer'],
        removelettes( row['Premium']),
        branch,
        '',
        '',
        '',
        '',
        '',
        createdAt,
        '',
        createdON,
        '',
        '',
        '',
        row['nEnd'],
        '',
        '',
        '',
        row['nCancel'],
        '',
        '',
        row['BinderNo'],
        '',
        '',
        '',
        '',
        '',
        '',
        row['nStart'].replace("Nil",""),
        removelettes(row['SumInsured']),
        '',
        '',
        '',
        '',
        row['PolicyNo']
    ])




dataOutput = pd.DataFrame(cleandData, columns=[
    'Account Code',
    'Annualized Prem',
    'Branch',
    'Cancel Date',
    'Cancel Reason Hdg',
    'Cancel Time',
    'Cancelled By',
    'Country',
    'Created At',
    'Created By',
    'Created On',
    'Currency',
    'Date for Renewal',
    'Date Proposal Signed',
    'End Date',
    'Endorsements that apply',
    'Inception Date',
    'Insured',
    'Is Cancelled',
    'Occupancy',
    'Policy End Time',
    'Policy No',
    'Policy Payment Plan No',
    'Policy Prefix',
    'Policy Start Time',
    'Prem_Finance_Name',
    'Source Comm Rate',
    'Source Name',
    'Start Date',
    'Sum Insured',
    'Warranties Do Not Apply',
    'Policy Limits of Liability ',
    'Policy Extensions ',
    'Joint Insured ',
    'Insurer Policy Number'
])

# displaying the DataFrame
# print('DataFrame:\n', dataOutput)

# saving the DataFrame as a CSV file
gfg_csv_data = dataOutput.to_csv('orions_policy.tsv', index=False, sep="\t")
gfg_csv_data = dataOutput.to_csv('orions_policy.csv', index=False)

# print('\nCSV String:\n', gfg_csv_data)

# print(df);

print(len(cleandData));

# print(df);
# %%
