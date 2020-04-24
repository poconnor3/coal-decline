#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:51:13 2020

@author: phoebe
"""
import requests
import pandas as pd

pd.set_option('display.max_rows',None)

csv = pd.read_csv('eia_variables.csv')
print("csv",csv)

eia_df = pd.DataFrame()

for eia_variable in csv['name']:  
    api = 'https://api.eia.gov/series/'
    key = '1ff1006b301ab895a5ddd60a473a44c2'
    payload = {'series_id':eia_variable, 'api_key':key }
    response = requests.get(api, payload)

    if response.status_code == 200:
        print("Request successful")
    else:
        print(response.status_code)
        print(response.text)
        assert False

    row_list = response.json()
    series = row_list['series']
    numbers = series[0]['data']
    data_df = pd.DataFrame(columns = ["year", "value"], data = numbers)
    data_df.set_index("year", inplace=True)
    numbers = data_df["value"]
    eia_df[eia_variable] = numbers

eia_df = eia_df.drop(['2002', '2003','2004', '2005','2006', '2007','2008', '2009','2010', '2011','2012', '2013','2014', '2015','2016', '2017', '2018'])

parts = eia_df.columns.str.split('-')
tups = [(p[0],p[1]) for p in parts]
ind = pd.MultiIndex.from_tuples(tups)
eia_df.columns = ind
eall = eia_df['ELEC.GEN.ALL']
ecow = eia_df['ELEC.GEN.COW']
cow_share = ecow/eall
pct_change = round(((cow_share.loc['2019'] - cow_share.loc['2001']) / cow_share.loc['2001']), 2)
pct_change_df = pd.DataFrame(columns = ["percent change in coal, 2001-2019"], data = pct_change)
pct_change_df.to_csv('percent_change.csv')