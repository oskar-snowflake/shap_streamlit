#Streamlit app on top of SHAP notebook
import json
from typing import Tuple, Iterable
from snowflake.snowpark.session import Session
import snowflake.snowpark.functions as F
import snowflake.snowpark.types as T
from snowflake.snowpark.functions import sproc, udtf, udf, pandas_udf

# Creating Snowpark Session
session = Session.builder.configs(snowflake_connection_cfg).create() USE STREAMLIT SECRETS MANAGER

# Switch schema
session.use_schema('ML_SHAP')

print('Role:     ', session.get_current_role())
print('Warehouse:', session.get_current_warehouse())
print('Database: ', session.get_current_database())
print('Schema:   ', session.get_current_schema())

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

snowpark_df_explained = session.table('ECOMMERCE_CUSTOMERS_100M_SHAP_VALUES')
snowpark_df_explained.limit(5).to_pandas()
