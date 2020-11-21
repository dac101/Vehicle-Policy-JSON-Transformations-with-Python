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
    accidentDateStr = ''
    reportDateStr = ''

    # result = binder.Query(row['ID'] == 'iIemID')

    # How to Query the panda database
    r = binder[binder.iIemID == row['iIemID']]
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
            sumInsuredT =  str(rr['SumInsured']).split(".")

            sumInsuredT = sumInsuredT[0]
            sumInsuredT = re.sub("[^0-9]", "", str(rr['SumInsured']))
            sumInsuredT = re.sub(r'[a-z]+', "",  sumInsuredT)
            r['PolicyNo'].fillna("", inplace=True)
            r['SumInsured'].fillna(0, inplace=True)
            r['Premium'].fillna("", inplace=True)


            policyNumber = rr['PolicyNo']
            #sumInsuredT = re.sub("[^0-9]", "", str(rr['SumInsured']))
            sumInsured = sumInsuredT
            print(sumInsured)

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

    accidentDate = str(row['AccidentDate']).split()
    reportDate = str(row['ReportDate']).split()

    if len(accidentDate) > 0:
        accidentDateStr = accidentDate[0]

    if len(reportDate) > 0:
        reportDateStr = reportDate[0]



    settle = False
    if row['Settle'] == 'Y':
        settle = True
    cleanData.append([
        '',
        '',
        '',
        '',
        row['ID'],
        '',
        accidentDateStr,
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        settle,
        '',
        '',
        email,
        nEnd,
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        row['Liability'],
        '',
        '',
        '',
        '',
        '',
        '',
        CurrentBI,
        CurrentOD,
        CurrentPD,
        '',
        '',
        '',
        '',
        '',
        policyNumber,
        riskDescription,
        riskId,
        '',
        status,
        sumInsured,
        vehCC,
        '',
        '',
        vehEngine,
        vehReg,
        vehChasis,
        '',
        vehReg,
        riskDescription,
        vehYear,
        '_cr_ AccidentDate' + str(row['AccidentDate']) + '_cr_ ReportDate' + str(
            reportDateStr) + '_cr_ Description' + str(row['Description']) + '_cr_ SettleAmount' +  str(row['SettleAmount'])

           + '_cr_ Insurer Policy Number' + str(row['PolicyNo'])

    ])

dataOutput = pd.DataFrame(cleanData, columns=[
    'Age of Driver at DOL',
    'Branch',
    'Broker Reference ID',
    'Catastrophic Event',
    'Claim ID',
    'Claims Handler',
    'Claims Year',
    'Closed At',
    'Closed By',
    'Closed On',
    'Created At',
    'Created By',
    'Created On',
    'Currency',
    'Current BI',
    'Current OD',
    'Current PD',
    'Email Address',
    'Expiry Date',
    'Initial BI',
    'Initial OD',
    'Initial PD',
    'Insured',
    'Is a Total Loss',
    'Is Closed',
    'Is No Report',
    'Lawyer Name',
    'Liable Party',
    'Limits of Liability',
    'Location No',
    'Location_Town_or_Area',
    'Locus of Event',
    'Loss Cause',
    'Loss Date',
    'Loss Result',
    'Loss Time',
    'Police Officer Details',
    'Police Station',
    'Police_Officer_Badge_No',
    'Policy Breach Details',
    'Policy Cover Start Date',
    'Policy Inception Date',
    'Policy No',
    'Risk Desc',
    'Risk Item No',
    'Source Name',
    'Status',
    'Sum Insured',
    'Veh CC Rating',
    'Veh Cylinders',
    'Veh Drivers Side',
    'Veh Engine No',
    'Veh Reg Owner',
    'Vehicle Chassis',
    'Vehicle ID',
    'Vehicle Reg No',
    'Vehicle Risk Description',
    'Vehicle Year',
    'Note',

])

# displaying the DataFrame
# print('DataFrame:\n', dataOutput)
print(len(cleanData))
print("reach")

# saving the DataFrame as a CSV file
gfg_csv_data = dataOutput.to_csv('orion_claims.tsv', index=False, sep="\t")
gfg_csv_data = dataOutput.to_csv('orion_claims.csv', index=False)

# print('\nCSV String:\n', gfg_csv_data)

# print(df);


print("finish")

# print(df);
# %%
