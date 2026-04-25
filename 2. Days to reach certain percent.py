# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:38:10 2024

@author: Arsalan Dawalatabad
"""

import pandas as pd
from datetime import datetime

final_dataframe = pd.DataFrame(columns=
                               ['COMPANY NAME', 'Symbol', 'ISSUE PRICE','DATE OF LISTING','Year of Listing','Month of Listing',
                                'Listing Price','HIGHEST_PRICE','HIGHEST_PRICE DATE', 'LOWEST_PRICE', 'LOWEST_PRICE DATE',
                                "DAY1_HIGHEST","DAY2_HIGHEST","DAY3_HIGHEST",
'Days to 10% of Issue Price','Date - 10% of Issue Price','High Price - 10% of Issue Price',
'Days to 20% of Issue Price','Date - 20% of Issue Price','High Price - 20% of Issue Price',
'Days to 30% of Issue Price','Date - 30% of Issue Price','High Price - 30% of Issue Price',
'Days to 40% of Issue Price','Date - 40% of Issue Price','High Price - 40% of Issue Price',
'Days to 50% of Issue Price','Date - 50% of Issue Price','High Price - 50% of Issue Price',
'Days to 60% of Issue Price','Date - 60% of Issue Price','High Price - 60% of Issue Price',
'Days to 70% of Issue Price','Date - 70% of Issue Price','High Price - 70% of Issue Price',
'Days to 80% of Issue Price','Date - 80% of Issue Price','High Price - 80% of Issue Price',
'Days to 90% of Issue Price','Date - 90% of Issue Price','High Price - 90% of Issue Price',
'Days to 100% of Issue Price','Date - 100% of Issue Price','High Price - 100% of Issue Price','Comment'
], dtype='object')

unpickled_df = pd.read_pickle(r"D:/Learning/Python/IPO Analysis using Excel/Output/nse_2020_21_22_23_24.pkl")

folder_path = r"D:\\Learning\\Python\\IPO Analysis using Excel\\input files"
file_name = "\\NSE_IPO_Extract_20240926.xlsx"



df_of_IPOs = pd.read_excel(folder_path+file_name, sheet_name='Input')

# company_number = 0

for company_number in range(len(df_of_IPOs)):

    company = df_of_IPOs["Symbol"].tolist()[company_number]
    
    final_dataframe.loc[company_number,'COMPANY NAME'] = df_of_IPOs['COMPANY NAME'].tolist()[company_number]
    
    print()
    print()
    print(str(company_number)+". "+df_of_IPOs['COMPANY NAME'].tolist()[company_number])
    
    final_dataframe.loc[company_number,'Symbol'] = df_of_IPOs["Symbol"].tolist()[company_number]
    final_dataframe.loc[company_number,'DATE OF LISTING'] = datetime.strptime(df_of_IPOs['DATE OF LISTING'].tolist()[company_number], '%d-%b-%Y' )
    final_dataframe.loc[company_number,'Year of Listing'] = final_dataframe.loc[company_number,'DATE OF LISTING'].year
    final_dataframe.loc[company_number,'Month of Listing'] = final_dataframe.loc[company_number,'DATE OF LISTING'].month
    

    final_dataframe.loc[company_number,'ISSUE PRICE'] = float(str(df_of_IPOs['ISSUE PRICE'].tolist()[company_number]).replace(',',''))
    
    issue_price = float(str(df_of_IPOs['ISSUE PRICE'].tolist()[company_number]).replace(',',''))
    list_date = df_of_IPOs['DATE OF LISTING'].tolist()[company_number]
    
    list_date = datetime.strptime(list_date, '%d-%b-%Y' )
    
    filtered_df = unpickled_df[unpickled_df['SYMBOL']==company]
    
    if len(filtered_df)==0:
        final_dataframe.loc[company_number,'Comment'] = "Company not found in Data"
        continue
    
    # list_date = filtered_df[filtered_df[' DATE1']==min(filtered_df[" DATE1"].tolist())].iloc[0][" DATE1"]
    
    try:
        final_dataframe.loc[company_number,'Listing Price'] = filtered_df[filtered_df[' DATE1']==list_date].iloc[0][" OPEN_PRICE"]
    except:
        final_dataframe.loc[company_number,'Comment'] = "DATE OF LIST mis-match"
        continue
    final_dataframe.loc[company_number,'HIGHEST_PRICE'] = filtered_df[filtered_df[' HIGH_PRICE']==max(filtered_df[" HIGH_PRICE"].tolist())].iloc[0][" HIGH_PRICE"]
    final_dataframe.loc[company_number,'HIGHEST_PRICE DATE'] = filtered_df[filtered_df[' HIGH_PRICE']==max(filtered_df[" HIGH_PRICE"].tolist())].iloc[0][' DATE1']
    final_dataframe.loc[company_number,'LOWEST_PRICE'] = filtered_df[filtered_df[' LOW_PRICE']==min(filtered_df[' LOW_PRICE'].tolist())].iloc[0][' LOW_PRICE']
    final_dataframe.loc[company_number,'LOWEST_PRICE DATE'] = filtered_df[filtered_df[' LOW_PRICE']==min(filtered_df[' LOW_PRICE'].tolist())].iloc[0][' DATE1']
    
    filtered_df = filtered_df.sort_values(by=[' DATE1'])
    filtered_df = filtered_df.reset_index()
    
    percent_reach = [1.1,1.2,1.3,1.4,1.5,
                     1.6,1.7,1.8,1.9,2]
    # reach=0
    for reach in range(len(percent_reach)):
        for i in range(len(filtered_df)):
            
            if filtered_df.iloc[i][' HIGH_PRICE'] >= float(str(percent_reach[reach]).replace(',',''))*issue_price:
            
                days_col_name = "Days to "+str(int(round(percent_reach[reach]-1,2)*100))+"% of Issue Price"
                date_col_name = "Date - "+str(int(round(percent_reach[reach]-1,2)*100))+"% of Issue Price"
                hp_col_name = "High Price - "+str(int(round(percent_reach[reach]-1,2)*100))+"% of Issue Price"
                
                final_dataframe.loc[company_number,days_col_name] = ((filtered_df.iloc[i][' DATE1'] - list_date).days)+1
                final_dataframe.loc[company_number,date_col_name] = filtered_df.iloc[i][' DATE1']
                final_dataframe.loc[company_number,hp_col_name] = filtered_df.iloc[i][' HIGH_PRICE']
                
                # print(str(reach)+" "+str(round(percent_reach[reach]-1,2)*100))
                print(f"{percent_reach[reach]} times --- {filtered_df.iloc[i][' DATE1']} --- "+str(filtered_df.iloc[i][' HIGH_PRICE']))
                print(f"List date --- "+str(list_date)+" --- "+str(issue_price))
                print(f"Days : "+str((filtered_df.iloc[i][' DATE1'] - list_date).days+1))
                break
            
# final_dataframe.to_excel("D:\\Learning\\Python\\IPO Analysis using Excel\\Output\\output.xlsx", sheet_name='Data')

with pd.ExcelWriter("D:\\Learning\\Python\\IPO Analysis using Excel\\Output\\output.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    final_dataframe.to_excel(writer, sheet_name='Data', index=False)

'''

Index(['COMPANY NAME', 'SECURITY TYPE', 'ISSUE PRICE', 'Symbol',
       'ISSUE START DATE', 'ISSUE END DATE', 'PRICE RANGE', 'DATE OF LISTING'],
      dtype='object')


        Date  Date_ddmmyyyy  ...  DELIV_QTY  DELIV_PER
0 2020-12-31       31122020  ...   231186.0      55.88
1 2020-12-31       31122020  ...     7348.0      99.90
2 2020-12-31       31122020  ...  2121071.0     100.00
3 2020-12-31       31122020  ...     2181.0      67.27
4 2020-12-31       31122020  ...     9574.0      86.36


Index(['Date', 'Date_ddmmyyyy', 'url', 'SYMBOL', ' SERIES', ' DATE1',
       ' PREV_CLOSE', ' OPEN_PRICE', ' HIGH_PRICE', ' LOW_PRICE',
       ' LAST_PRICE', ' CLOSE_PRICE', ' AVG_PRICE', ' TTL_TRD_QNTY',
       ' TURNOVER_LACS', ' NO_OF_TRADES', ' DELIV_QTY', ' DELIV_PER'],
      dtype='object')

'''