import pandas as pd

# Read the raw_customers.csv file
raw_customers_df = pd.read_csv('raw_customers.csv')

# Save the data to stg_customers.csv without any changes
raw_customers_df.to_csv('stg_customers.csv', index=False)

print("Data has been saved to stg_customers.csv successfully.")
