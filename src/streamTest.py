import streamlit as st
import numpy as np
import pandas as pd
import re

message = st.chat_message("assistant")
message.write("Hello human")

# data = {"calories": ["big", "Med", "Sml"], "duration": [50, 40, 45]}

# load data into a DataFrame object:
# df = pd.DataFrame(data)

# message.bar_chart(df, x=list(df.columns)[0], y=list(df.columns)[1])

response = f"""SELECT VALUE FROM FROSTY_SAMPLE.CYBERSYN_FINANCIAL.FINANCIAL_ENTITY_ANNUAL_TIME_SERIES LIMIT 10;"""

message = {"role": "assistant", "content": response}
# Parse the response for a SQL query and execute if available
sql_match = re.search(r"```sql\n(.*)\n```", response, re.DOTALL)
if sql_match:
    print("SQL MATCH")
else:
    print("Not SQL MATCH")
