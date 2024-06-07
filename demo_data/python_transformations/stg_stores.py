import pandas as pd

# Read the raw_stores.csv file
source_df = pd.read_csv('raw_stores.csv')

# Rename the columns as specified
renamed_df = source_df.rename(columns={
    'id': 'location_id',
    'name': 'location_name',
    'tax_rate': 'tax_rate',
    'opened_at': 'opened_date'
})

# Select the desired columns
renamed_df = renamed_df[[
    'location_id',
    'location_name',
    'tax_rate',
    'opened_date'
]]

# Display the final DataFrame
print(renamed_df)

# Save the result to stg_stores.csv
renamed_df.to_csv('stg_stores.csv', index=False)

print("Data has been saved to stg_stores.csv successfully.")
