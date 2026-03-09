# Insurance Data Simulation & Analytics

## Overview

This project simulates an insurance company's policy sales and claim activity in order to analyze risk exposure and portfolio profitability. The dataset contains one million policy records generated for the year 2024 and simulated claims occurring in 2025 and early 2026.

The objective of the project is to demonstrate data simulation, analytical querying, and insight generation using Python.

## Dataset Description

Two datasets were generated:

### Policy Sales Data
Contains simulated insurance policy records.

Fields:
- Customer_ID
- Vehicle_ID
- Vehicle_Value
- Premium
- Policy_Purchase_Date
- Policy_Start_Date
- Policy_End_Date
- Policy_Tenure

### Claims Data
Contains simulated claim records.

Fields:
- Claim_ID
- Customer_ID
- Vehicle_ID
- Claim_Amount
- Claim_Date
- Claim_Type

Claim amount = 10% of vehicle value.

## Assumptions

- Total policies: 1,000,000
- Vehicle value: ₹100,000
- Premium = ₹100 × policy tenure
- Policy start date = purchase date + 365 days
- Tenure distribution:
  - 20% 1-year policies
  - 30% 2-year policies
  - 40% 3-year policies
  - 10% 4-year policies

## Claims Logic

### Claims in 2025
Vehicles purchased on the 7th, 14th, 21st, and 28th of each month have a 30% probability of filing a claim.

### Claims in 2026
10% of vehicles with 4-year policy tenure file claims between January 1 and February 28, 2026.

## Analysis Performed

The following analyses were performed:

1. Total premium collected in 2024
2. Total claim cost with monthly breakdown
3. Claim cost to premium ratio by policy tenure
4. Claim ratio by policy purchase month
5. Potential future claim liability
6. Earned premium estimation

## Visualizations

Charts created:

- Monthly claim trend
- Claims by year
- Claims by policy tenure

## Key Insights

- Claim events are concentrated on specific purchase dates due to simulated defect patterns.
- Longer policy tenures increase the insurer's exposure to claim risk.
- A significant portion of premium collected remains unearned and will be recognized over the remaining policy period.

## Tools Used

- Python
- Pandas
- Matplotlib

## Author

Kartikey Mishra
