## Step 1: import Python libraries and dataset, perform EDA

# %%

# !pip install rake_nltk
from datetime import datetime

import pandas as pd
import numpy as np
import re
import warnings

warnings.filterwarnings("ignore")


def removelettes(x):
    sumInsuredT = str(x).split(".")
    sumInsuredT = sumInsuredT[0]
    sumInsuredT = re.sub("[^0-9]", "", sumInsuredT)
    sumInsuredT = re.sub(r'[a-z]+', "", sumInsuredT)
    return sumInsuredT


def removelettesOnly(x):
    # sumInsuredT = re.sub("[^0-9]", "", str(x))
    sumInsuredT = re.sub(r'[a-z]+', "", x)
    return sumInsuredT


# df = pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xxeevdialfl7')   # 250 rows × 38 columns
df = pd.read_csv('CustomerOrions.csv')  # same data 250 rows × 38 columns
# create the pandas dataframe

cleandData = []

for index, row in df.iterrows():
    # print(row,index);
    # print(row['Id'], row['First'])

    # remove the

    email = ''
    dob = ''
    tels = removelettesOnly(str((str(row['Tel'])).lower().replace("-", "").replace("or", "/")))
    cells = removelettesOnly(str((str(row['Cell'])).lower().replace("-", "").replace("or", "/")))
    tels = re.sub(r'[a-z]+', '', tels, re.I)
    cells = re.sub(r'[a-z]+', '', cells, re.I)
    tels =  str(tels).replace(".","").replace("()","")
    cells = str(cells).replace(".","").replace("()","")

    print(tels)
    print(cells)
    if "@" in str(row['Email']):
        email = row['Email']

    if "00:00:00" != str(row['DOB']):
        dob = str(row['DOB'])

    if "1801-01-01" == str(row['DOB']) or "1866-08-17" == str(row['DOB']) or "1859-08-22" == str(row['DOB']):
        dob = ""
    print(row['DOB'])
    dob = dob.replace("nan", "")
    if ("&" in row['First']) or ("/" in row['First']):
        # print(row['First'] + " " + str(row['Last']))
        splitor = '&'
        if ("/" in row['First']):
            splitor = "/"

        splitsFirstName = str(row['First']).split(splitor)
        splitsLastName = str(row['Last']).split(splitor)
        splitsLastTrn = []

        if "/" in str(row['TRN']):
            splitsLastTrn = str(row['TRN']).split("/")


        # if "/" in str(row['Tel']) or "or" in str(row['Tel']):
        #
        #     # telephone = removelettes(telephone)
        #
        #     if "or" in str(row['Tel']):
        #         tell = str(row['Tel']).split("or")
        #     else:
        #         tels = str(row['Tel']).replace("-", "")
        #         cells = str(row['Cell']).replace("-", "")
        #
        #         telephone = str(row['Tel']).replace(" ", "/")
        #         tell = str(telephone).split("/")
        #
        #     tels = ''
        #     counter = 0
        #     for te in tell:
        #         te = removelettesOnly(te)
        #         number = ''.join(i for i in te if i.isdigit())
        #
        #         if len(number) == 7:
        #             number = '876' + number
        #
        #         if counter > 0:
        #             if number != '':
        #                 number = removelettesOnly(number)
        #                 tels = tels + '/' + number
        #         else:
        #             number = removelettesOnly(number)
        #             tels = tels + number
        #         counter = counter + 1
        # else:
        #     tels = removelettesOnly(row['Tel'])
        #     tels = ''.join(i for i in str(tels) if i.isdigit())
        #     if len(str(tels)) == 7:
        #         tels = '876' + str(tels)
        #
        # if "/" in str(row['Cell']):
        #     if "or" in str(row['Tel']):
        #         tell = str(row['Tel']).split("or")
        #     else:
        #         telephone = str(row['Cell']).replace(" ", "/")
        #         tell = str(telephone).split("/")
        #
        #     cells = ''
        #     counter = 0
        #     for te in tell:
        #         te = removelettesOnly(te)
        #         number = ''.join(i for i in te if i.isdigit())
        #
        #         if len(number) == 7:
        #             number = '876' + number
        #
        #         if counter > 0:
        #             if number != '':
        #                 number = removelettesOnly(number)
        #                 cells = cells + '/' + number
        #         else:
        #             number = removelettesOnly(number)
        #             cells = cells + number
        #         counter = counter + 1
        # else:
        #     cells = removelettesOnly(row['Cell'])
        #     cells = ''.join(i for i in str(cells) if i.isdigit())
        #     if len(cells) == 7:
        #         cells = '876' + cells

        for firstName in splitsFirstName:
            counter = 0
            if len(splitsLastTrn) > 1:
                trn = splitsLastTrn[counter]
            else:
                trn = row['TRN']

            # print(firstName + splitsLastName[counter])
            trn = str(trn).replace(" ", "").replace("`", "").replace("nan", "").replace("-", ""),
            trn = ''.join(i for i in trn if i.isdigit())
            # cells = removelettes(cells)
            # tels = removelettes(tels)
            cleandData.append([
                '',
                '',
                dob,
                '',
                '',
                '',
                '',
                '',
                '',
                email,
                '',
                firstName,
                '',
                '',
                False,
                splitsLastName[counter],
                '',
                '',
                row['Address'],
                '',
                '',
                trn,
                'TRN',
                '',
                row['Occupation'],
                '',
                tels,
                cells,
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
                row['Id']
            ])

            if len(splitsLastName) == 2:
                counter = counter + 1


    else:
        companyName = ""
        is_a_company_false = False
        if ("co." in str(row['First']).lower()) or ("co." in str(row['Last']).lower()):
            companyName = str(row['First']) + " " + str(row['Last'])
            is_a_company_false = True

        trn = str(row['TRN']).replace(" ", "").replace("`", "").replace("nan", "").replace("-", ""),
        trn = ''.join(i for i in trn if i.isdigit())
        # cells = removelettes(cells)
        # tels = removelettes(tels)
        cleandData.append([
            companyName,
            '',
            dob,
            '',
            '',
            '',
            '',
            '',
            '',
            email,
            '',
            row['First'],
            '',
            '',
            is_a_company_false,
            row['Last'],
            '',
            '',
            row['Address'],
            '',
            '',
            trn,
            'TRN',
            '',
            row['Occupation'],
            '',
            tels,
            cells,
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
            row['Id'],
        ])

    # break;

dataOutput = pd.DataFrame(cleandData, columns=[
    'Company Name',
    'Country_Of_Residence',
    'Date of Birth',
    'Drivers Licence Country',
    'Drivers Licence Date Issued',
    'Drivers Licence Expiry Date',
    'Drivers Licence First Issued',
    'Drivers Licence Number',
    'Drivers Licence Type',
    'Email Address',
    'Employment Type',
    'First Name',
    'Gender',
    'Global_Name_No',
    'Is A Company',
    'Last Name',
    'Location No',
    'Maiden Name',
    'Mailing Address',
    'Marital Status',
    'Middle Name',
    'National ID',
    'National ID Type',
    'Nationality',
    'Occupation',
    'Phone_No_Fax',
    'Phone_No_General',
    'Phone_No_Mobile',
    'Place of Birth',
    'POCA Expiry Date',
    'POCA_Doc_For_Type',
    'POCA_Doc_Proof_of_Addr',
    'POCA_Docs_Received',
    'POSI Reason',
    'POSI Type',
    'Tax ID No',
    'Taxi_Badge_Date_Expires',
    'Taxi_Badge_Date_Issued',
    'Taxi_Badge_Number',
    'Title',
    'Idempo'
])

# displaying the DataFrame
# print('DataFrame:\n', dataOutput)

# saving the DataFrame as a CSV file
gfg_csv_data = dataOutput.to_csv('orions_customers.tsv', index=False, sep="\t")
gfg_csv_data = dataOutput.to_csv('orions_customers.csv', index=False)
# print('\nCSV String:\n', gfg_csv_data)

# print(df);

print(len(cleandData));

# print(df);
# %%
