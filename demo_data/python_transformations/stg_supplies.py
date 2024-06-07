import pandas as pd

# Read the raw_supplies.csv file
source_df = pd.read_csv('raw_supplies.csv')

# Rename the columns as specified
renamed_df = source_df.rename(columns={
    'id': 'supply_id',
    'sku': 'product_id',
    'name': 'supply_name',
    'cost': 'supply_cost',
    'perishable': 'is_perishable_supply'
})

# Select the desired columns
renamed_df = renamed_df[[
    'supply_id',
    'product_id',
    'supply_name',
    'supply_cost',
    'is_perishable_supply'
]]

# Display the final DataFrame
print(renamed_df)

# Save the result to stg_supplies.csv
renamed_df.to_csv('stg_supplies.csv', index=False)

print("Data has been saved to stg_supplies.csv successfully.")
