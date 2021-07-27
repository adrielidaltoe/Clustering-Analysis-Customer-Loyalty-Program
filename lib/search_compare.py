import pandas as pd
import numpy as np

def search_match_products(customer_list, valid_transactions, return_transactions, time_interval):
    
    '''Search for products that appear simultaneously in two transactions within a period of time of 25 days.
    Parameters:
    -----------
    customer_list: list with CustomerID.
    valid_transactions: dataframe with valid transactions
    return_transactions: dataframe with return transactions
    time_interval: integer. Time interval in days.
    '''
    
    match = dict()
    for customer in customer_list:
        filter_customer_val_transactions = valid_transactions[valid_transactions['CustomerID']==customer]
        filter_return_transactions = return_transactions[return_transactions['CustomerID']==customer]
        match[customer] = list()
    
        for c_transaction in filter_return_transactions['InvoiceNo'].values:
            products_C_transaction = filter_return_transactions[filter_return_transactions['InvoiceNo']==c_transaction]\
                                                    	       ['StockCode'].values[0]
            matched_transaction_list = [c_transaction]
            for transaction in filter_customer_val_transactions['InvoiceNo'].values:
                products = filter_customer_val_transactions[filter_customer_val_transactions['InvoiceNo']==transaction]\
                                                           ['StockCode'].values[0]
            
                date_v = filter_customer_val_transactions[filter_customer_val_transactions['InvoiceNo']==transaction]\
                                                         ['InvoiceDate'].values[0]
                date_c = filter_return_transactions[filter_return_transactions['InvoiceNo']==c_transaction]\
                                                   ['InvoiceDate'].values[0]
            
                max_date = date_v + np.timedelta64(time_interval,'D')
            
                if date_c >= date_v and date_c <= max_date:
                    if len(products_C_transaction.intersection(products)) > 0:
                        matched_transaction_list.append(transaction)
            match[customer].append(matched_transaction_list)
    return match