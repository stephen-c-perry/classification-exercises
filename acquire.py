import os
import pandas as pd
import env



def pull_titanic_data():
    sql_query= 'SELECT * FROM passengers'
    df = pd.read_Sql(sql_query, env.get_connection('titanic_db'))
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
    sql_query = '''
                SELECT
                    species_id,
                    species_name,
                    sepal_length,
                    sepal_width,
                    petal_length,
                    petal_width
                FROM measurements
                JOIN species USING(species_id
                '''
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
    sql_query = '''
                SELECT * FROM customers
                JOIN contract_types USING (contract_type_id)
                JOIN internet_service_types USING (contract_type_id)
                JOIN payment_types using (payment_type_id)
                '''
    df = pd.read_sql(sql_query, env.get_connection('telco_churn'))
    return df

def get_telco_data():
    if os.path.isfile('telco.csv'):
        df = pd.read_csv('telco.csv', index_col = 0)
    else:
        df = pull_iris_data()
        df.to_csv('telco.csv')
    return df


# Once you've got your get_titanic_data, get_iris_data, and get_telco_data 
# functions written, now it's time to add caching to them. To do this, edit the
#  beginning of the function to check for the local filename of
#  telco.csv, titanic.csv, or iris.csv. If they exist, use the .csv file.
#  If the file doesn't exist, then produce the SQL and pandas necessary to create a
#  dataframe, then write the dataframe to a .csv file with the appropriate name.


