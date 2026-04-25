# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:42:41 2024

@author: Arsalan Dawalatabad
"""


import pandas as pd

combined_df_company_codes = []

for x in range(1,3426,200):
    if x < 3401 :
        try:
            df1 = pd.read_html("https://money.rediff.com/companies/nseall/"+str(x)+"-"+str(x+199))[1]
            # print(str(x)+"-"+str(x+199))
            combined_df_company_codes.append(df1)
        except:
            print(str(x)+"-"+str(x+199)+"[1] is not present")
            
        try:
            df1 = pd.read_html("https://money.rediff.com/companies/nseall/"+str(x)+"-"+str(x+199))[2]
            combined_df_company_codes.append(df1)
        except:
            print(str(x)+"-"+str(x+199)+"[2] is not present")
    else:
        df1 = pd.read_html("https://money.rediff.com/companies/nseall/"+str(x)+"-3425")[0]
        combined_df_company_codes.append(df1)
        # print(str(x)+"-3425")
        break

# Concatenate all DataFrames into one
combined_data = pd.concat(combined_df_company_codes, ignore_index=True)

combined_data.to_excel(r'D:\Learning\Python\IPO Analysis using Excel\Data\Company Codes.xlsx')


# df1 = pd.read_html("https://money.rediff.com/companies/nseall/"+str(3400)+"-3425")
