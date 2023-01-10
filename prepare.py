import env
import acquire
import pandas as pd
from sklearn.model_selection import train_test_split

'''
The three functions below (prep_iris, prep_titanic, prep_telco) take in the corresponding
datasets and cleans them by dropping, encoding, concatenating, changing data types, etc
'''


def prep_iris(iris):
    iris = iris.drop(columns=['species_id'])
    iris.rename(columns={'species_name': 'species'}, inplace=True)
    species_encoded = pd.get_dummies(iris.species, drop_first=True)
    iris = pd.concat([iris, species_encoded], axis=1)
    return iris

# prepped_iris = prep_iris(acquire.get_iris_data())



# titanic

#def prep_titanic(titanic_df):
 #   titanic_df = titanic_df = titanic_df.drop(columns=['deck', 'age'])
  #  dummies = pd.get_dummies(titanic_df[['embark_town', 'sex']], drop_first=True)
   # titanic_df = pd.concat([titanic_df, dummies], axis=1)
    #return titanic_df

# the above function did not sufficiently clean the titanic data.  correction below

# prepped_titanic = prep_titanic(acquire.get_titanic_data())



def prep_titanic(titanic_df):

    titanic_df = titanic_df.drop_duplicates()
    cols_to_drop = ['deck', 'embarked', 'class', 'passenger_id']
    titanic_df = titanic_df.drop(columns=cols_to_drop)
    titanic_df['embark_town'] = titanic_df.embark_town.fillna(value='Southampton')
    dummy_df = pd.get_dummies(titanic_df[['sex', 'embark_town']], dummy_na=False, drop_first=[True])
    titanic_df = titanic_df.drop(columns=['sex'])
    titanic_df = pd.concat([titanic_df, dummy_df], axis=1)
    
    return titanic_df


#telco
def prep_telco(telco_df):

    telco_df = telco_df.drop(columns = ['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    telco_df.total_charges = (telco_df.total_charges + '0').astype('float')

    categorical_cols = []
    binary_categories = []
    multi_categories = []
    numerical_cols = []

    for col in telco_df:
        if telco_df[col].dtype == 'object':
            categorical_cols.append(col)
        if telco_df[col].value_counts().size > 2:
            multi_categories.append(col)
        else:
            binary_categories.append(col)
    else:
        numerical_cols.append(col)

    telco_df.gender = telco_df.gender.replace('Male',1)
    telco_df.dependents = telco_df.dependents.replace('Yes', 1).replace('No', 0)
    telco_df.phone_service = telco_df.phone_service.replace('Yes', 1).replace('No', 0)
    telco_df.paperless_billing = telco_df.paperless_billing.replace('Yes', 1).replace('No', 0)
    telco_df.partner = telco_df.partner.replace('Yes', 1).replace('No',0)

    return telco_df

# prepped_telco = prep_telco(acquire.get_telco_data())


# Split Data (train, validate, test)
'''
split_data is a function that takes in a dataframe and a specified target column, splits that data first into train and 
test dataframes, then splits the train set further into train and validate.  This results in 3 dataframes to use for modeling.
'''
def split_data(df, target=''):
    train, test = train_test_split(df, 
                               train_size = 0.8,
                               random_state=1349,
                              stratify=df[target])
    train, val = train_test_split(train,
                             train_size = 0.7,
                             random_state=1349,
                             stratify=train[target])
    return train, val, test

    # Need train_test_split function^


#spit function

def my_train_test_split(df, target):
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[target])
    train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train[target])
    return train, validate, test


def split_data(df):
    train_validate, test = train_test_split(df, test_size=0.2, random_state=123, stratify=df.survived)
    train, validate = train_test_split(train_validate, 
                                       test_size=0.3, 
                                       random_state=123, 
                                       stratify=train_validate.survived)
    return train, validate, test