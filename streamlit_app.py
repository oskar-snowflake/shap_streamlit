#Streamlit app on top of SHAP notebook
import json
from typing import Tuple, Iterable
from snowflake.snowpark.session import Session
import snowflake.snowpark.functions as F
import snowflake.snowpark.types as T
from snowflake.snowpark.functions import sproc, udtf, udf, pandas_udf

import shap
import pandas as pd

import streamlit as st



# Creating Snowpark Session
def create_session_object():
   connection_parameters = {
    "account": st.secrets["account"],
    "user": st.secrets["user"],
    "role": st.secrets["role"],
    "password": st.secrets["password"],
    "database": st.secrets["database"],
    "schema": st.secrets["schema"],
    "warehouse": st.secrets["warehouse"]
    }
   session = Session.builder.configs(connection_parameters).create()
   return session

feature_cols = ['AVG_SESSION_LENGTH', 
                'TIME_ON_APP',
                'TIME_ON_WEBSITE',
                'MEMBERSHIP_LENGTH',
                'GENDER_FEMALE',
                'GENDER_MALE',
                'MEMBERSHIP_STATUS_BASIC',
                'MEMBERSHIP_STATUS_BRONZE',
                'MEMBERSHIP_STATUS_SILVER',
                'MEMBERSHIP_STATUS_GOLD',
                'MEMBERSHIP_STATUS_PLATIN',
                'MEMBERSHIP_STATUS_DIAMOND']

def load_data(session):
    #Explained rows
    df_exp = snowpark_df_explained = session.table('ECOMMERCE_CUSTOMERS_100M_SHAP_VALUES').limit(10).to_pandas()
    st.dataframe(df_exp)

if __name__ == "__main__":
    session = create_session_object()
    load_data(session)
    
