import pandas as pd
import matplotlib.pyplot as plt

# load data
policy = pd.read_csv("policy_sales_data.csv")
claims = pd.read_csv("claims_data.csv")

# convert date
claims["Claim_Date"] = pd.to_datetime(claims["Claim_Date"])

# extract month and year
claims["Month"] = claims["Claim_Date"].dt.month
claims["Year"] = claims["Claim_Date"].dt.year

# CLAIM TREND BY MONTH
monthly_claims = claims.groupby("Month")["Claim_Amount"].sum()

plt.figure()
monthly_claims.plot(kind="line", marker="o")
plt.title("Monthly Claim Trend")
plt.xlabel("Month")
plt.ylabel("Claim Amount")
plt.savefig("claim_trend.png")

# CLAIMS BY YEAR
year_claims = claims.groupby("Year")["Claim_Amount"].sum()

plt.figure()
year_claims.plot(kind="bar")
plt.title("Claims by Year")
plt.xlabel("Year")
plt.ylabel("Claim Amount")
plt.savefig("claims_by_year.png")

# CLAIMS BY POLICY TENURE
merged = claims.merge(policy,on=["Customer_ID","Vehicle_ID"])

tenure_claims = merged.groupby("Policy_Tenure")["Claim_Amount"].sum()

plt.figure()
tenure_claims.plot(kind="bar")
plt.title("Claims by Policy Tenure")
plt.xlabel("Tenure")
plt.ylabel("Claim Amount")
plt.savefig("claims_by_tenure.png")

print("Dashboard charts created")