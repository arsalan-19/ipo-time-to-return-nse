# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:31:51 2024

@author: Arsalan Dawalatabad
"""

import pandas as pd
import os

def read_stock_data():
    print("Reading Files...")
    folder_path = r'D:\Learning\Python\IPO Analysis using Excel\Data'
    
    complete_data = pd.DataFrame()
    all_files_names = os.listdir(folder_path)
    
    all_files_with_path = []
    
    for x in range(0,len(all_files_names)):
        if all_files_names[x].startswith('NSE Stock') and all_files_names[x].endswith('.xlsx'):
            all_files_with_path.append(folder_path+"\\"+all_files_names[x])
    
    for file in all_files_with_path:
        # file = all_files_with_path[1]
        data = pd.read_excel(file, sheet_name='Data')
        complete_data = pd.concat([complete_data, data], ignore_index=True)        
        print(file)
    
    return complete_data


if __name__ == '__main__':
    complete_data = read_stock_data()
    print("Reading Complete")
    
    complete_data.to_pickle(r"D:/Learning/Python/IPO Analysis using Excel/Output/nse_2020_21_22_23_24.pkl")
    
    # To read a pickle file
    # unpickled_df = pd.read_pickle(r"D:/Learning/Python/IPO Analysis using Excel/Output/complete_data.pkl")
