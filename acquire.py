import os
import pandas as pd
import env


'''
the pull% functions below create a function with a sql query to get the desired dataset from the sql server.  the get% functions
below first check for a csv file of the desired dataset, if the csv does not exist it uses the pull% function to request the data 
from the sql server then exports it to save locally as a csv and returns the dataframe
'''


def pull_titanic_data():
    sql_query= 'SELECT * FROM passengers'
    df = pd.read_sql(sql_query, env.get_connection('titanic_db'))
    return df

def get_titanic_data():
    if os.path.isfile('titanic.csv'):
        df = pd.read_csv('titanic.csv')
    else:
        df = pull_titanic_data()
        df.to_csv('titanic.csv')
    return df

#Make a function named get_iris_data

def pull_iris_data():
    sql_query = 'SELECT * FROM measurements JOIN species USING(species_id)'
    df = pd.read_sql(sql_query, env.get_connection('iris_db'))
    return df

def get_iris_data():
    if os.path.isfile('iris_df.csv'):
        df = pd.read_csv('iris_df.csv', index_col = 0)
    else:
        df = pull_iris_data()
        df.to_csv('iris_df.csv')
    return df
    


#Make a function named get_telco_data

def pull_telco_data():
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    df = pd.read_sql(sql_query, env.get_connection('telco_churn'))
    return df

def get_telco_data():
    if os.path.isfile('telco.csv'):
        df = pd.read_csv('telco.csv', index_col=0)
    else:
        df = pull_telco_data()
        df.to_csv('telco.csv')
    return df






