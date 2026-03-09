import pandas as pd
import numpy as np

df = pd.read_csv("policy_sales_data.csv")

claims = []

claim_dates_2025 = [7,14,21,28]

claim_id = 1

for i,row in df.iterrows():

    purchase_day = int(str(row["Policy_Purchase_Date"])[8:10])

    if purchase_day in claim_dates_2025:
        if np.random.rand() < 0.30:

            claim = {}
            claim["Claim_ID"] = claim_id
            claim["Customer_ID"] = row["Customer_ID"]
            claim["Vehicle_ID"] = row["Vehicle_ID"]
            claim["Claim_Amount"] = 100000 * 0.10
            claim["Claim_Date"] = row["Policy_Start_Date"]
            claim["Claim_Type"] = 1

            claims.append(claim)

            claim_id +=1

claims_df = pd.DataFrame(claims)

claims_df.to_csv("claims_data_2025.csv",index=False)

print("Claims data generated")

#claims for 2026
df = pd.read_csv("policy_sales_data.csv")

claims = []

four_year = df[df["Policy_Tenure"]==4]

sample = four_year.sample(frac=0.10)

dates = pd.date_range("2026-01-01","2026-02-28")

claim_id = 500000

for i,row in sample.iterrows():

    claim = {}

    claim["Claim_ID"] = claim_id
    claim["Customer_ID"] = row["Customer_ID"]
    claim["Vehicle_ID"] = row["Vehicle_ID"]
    claim["Claim_Amount"] = 100000 * 0.10
    claim["Claim_Date"] = np.random.choice(dates)
    claim["Claim_Type"] = 2

    claims.append(claim)

    claim_id +=1

claims_df = pd.DataFrame(claims)

claims_df.to_csv("claims_data_2026.csv",index=False)

#combines claims
import pandas as pd

c1 = pd.read_csv("claims_data_2025.csv")
c2 = pd.read_csv("claims_data_2026.csv")

claims = pd.concat([c1,c2])

claims.to_csv("claims_data.csv",index=False)

#total premium 2024
df = pd.read_csv("policy_sales_data.csv")

total_premium = df["Premium"].sum()

print(total_premium)

#Claim Cost per Year and Month

claims = pd.read_csv("claims_data.csv")

claims["Claim_Date"] = pd.to_datetime(claims["Claim_Date"])

claims["Year"] = claims["Claim_Date"].dt.year
claims["Month"] = claims["Claim_Date"].dt.month

result = claims.groupby(["Year","Month"])["Claim_Amount"].sum()

print(result)

#Claim Ratio by Tenure
merged = claims.merge(df, on=["Customer_ID","Vehicle_ID"])

ratio = merged.groupby("Policy_Tenure")["Claim_Amount"].sum() / df.groupby("Policy_Tenure")["Premium"].sum()

print(ratio)

#Claim Ratio by Sales Month

df["Month"] = pd.to_datetime(df["Policy_Purchase_Date"]).dt.month

merged = claims.merge(df,on=["Customer_ID","Vehicle_ID"])

ratio = merged.groupby("Month")["Claim_Amount"].sum() / df.groupby("Month")["Premium"].sum()

print(ratio)

#Potential Future Claim Liability

claimed = claims["Vehicle_ID"].unique()

remaining = df[~df["Vehicle_ID"].isin(claimed)]

potential_liability = remaining.shape[0] * 10000

print(potential_liability)

#Earned Premium
#Daily Premium = Premium / (Tenure * 365)
df["Tenure_Days"] = df["Policy_Tenure"] * 365
df["Daily_Premium"] = df["Premium"] / df["Tenure_Days"]

