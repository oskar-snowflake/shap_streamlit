#Streamlit app on top of SHAP notebook
import json
from typing import Tuple, Iterable
from snowflake.snowpark.session import Session
import snowflake.snowpark.functions as F
import snowflake.snowpark.types as T
from snowflake.snowpark.functions import sproc, udtf, udf, pandas_udf

import shap
import pandas as pd

snowflake_connection_cfg = {
    "account": st.secrets["account"],
    "user": st.secrets["user"],
    "role": st.secrets["role"],
    "password": st.secrets["password"],
    "database": st.secrets["database"],
    "schema": st.secrets["schema"],
    "warehouse": st.secrets["warehouse"]
}

# Creating Snowpark Session
session = Session.builder.configs(snowflake_connection_cfg).create()

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
df = snowpark_df_explained.limit(5).to_pandas()
st.dataframe(df)
