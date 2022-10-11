from decimal import Decimal
from unicodedata import decimal
import pandas as pd
from decimal import *

var = pd.read_excel("data/sales_data.xlsx")

def get_team_data():
    data = {}
    for i in range(len(var)):
        if var['_SalesTeamID'][i] not in data:
            data[var['_SalesTeamID'][i]] = {
                'total_unit_cost': 0,
                'total_unit_price': 0,
                'total_discount_applied': 0,
                'total_order_quantity': 0,
                'total_profit_without_discount': 0,
                'total_profit_with_discount': 0,
            }
        data[var['_SalesTeamID'][i]]['team_id'] = (var['_SalesTeamID'][i])
        data[var['_SalesTeamID'][i]]['total_unit_cost'] += (var['Unit Cost'][i])
        data[var['_SalesTeamID'][i]]['total_unit_price'] += (var['Unit Price'][i])
        data[var['_SalesTeamID'][i]]['total_discount_applied'] += (var['Discount Applied'][i])
        data[var['_SalesTeamID'][i]]['total_order_quantity'] += (var['Order Quantity'][i])
        data[var['_SalesTeamID'][i]]['total_profit_without_discount'] += (var['Unit Price'][i] - var['Unit Cost'][i])
        data[var['_SalesTeamID'][i]]['total_profit_with_discount'] += ((var['Unit Price'][i] - (var['Unit Price'][i] * var['Discount Applied'][i])) - var['Unit Cost'][i])
    return data

def get_store_data():
    data = {}
    for i in range(len(var)):
        if var['_StoreID'][i] not in data:
            data[var['_StoreID'][i]] = {
                'total_unit_cost': 0,
                'total_unit_price': 0,
                'total_discount_applied': 0,
                'total_order_quantity': 0,
                'total_profit_without_discount': 0,
                'total_profit_with_discount': 0,
            }
        data[var['_StoreID'][i]]['store_id'] += (var['_StoreID'][i])
        data[var['_StoreID'][i]]['total_unit_cost'] += (var['Unit Cost'][i])
        data[var['_StoreID'][i]]['total_unit_price'] += (var['Unit Price'][i])
        data[var['_StoreID'][i]]['total_discount_applied'] += (var['Discount Applied'][i])
        data[var['_StoreID'][i]]['total_order_quantity'] += (var['Order Quantity'][i])
        data[var['_StoreID'][i]]['total_profit_without_discount'] += (var['Unit Price'][i] - var['Unit Cost'][i])
        data[var['_StoreID'][i]]['total_profit_with_discount'] += ((var['Unit Price'][i] - (var['Unit Price'][i] * var['Discount Applied'][i])) - var['Unit Cost'][i])
    return data