import pandas as pd
import numpy as np
from datetime import datetime, timedelta

num_customers = 1000000

# Date range
dates = pd.date_range(start="2024-01-01", end="2024-12-31")

# distribute policies evenly across dates
purchase_dates = np.random.choice(dates, num_customers)

# tenure distribution
tenure_choices = [1,2,3,4]
tenure_prob = [0.2,0.3,0.4,0.1]

tenure = np.random.choice(tenure_choices, num_customers, p=tenure_prob)

df = pd.DataFrame()

df["Customer_ID"] = range(1,num_customers+1)
df["Vehicle_ID"] = range(1000001,1000001+num_customers)
df["Vehicle_Value"] = 100000

df["Policy_Purchase_Date"] = purchase_dates
df["Policy_Tenure"] = tenure

df["Premium"] = df["Policy_Tenure"] * 100

df["Policy_Start_Date"] = df["Policy_Purchase_Date"] + pd.Timedelta(days=365)
df["Policy_End_Date"] = df["Policy_Start_Date"] + pd.to_timedelta(df["Policy_Tenure"]*365, unit="D")

df.to_csv("policy_sales_data.csv", index=False)

print("Policy dataset created")