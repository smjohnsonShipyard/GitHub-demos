import pandas as pd

# Read the raw_products.csv file
source_df = pd.read_csv('raw_products.csv')

# Rename the columns as specified
renamed_df = source_df.rename(columns={
    'sku': 'product_id',
    'name': 'product_name',
    'type': 'product_type',
    'description': 'product_description',
    'price': 'product_price'
})

# Select the desired columns
renamed_df = renamed_df[[
    'product_id',
    'product_name',
    'product_type',
    'product_description',
    'product_price'
]]

# Display the final DataFrame
print(renamed_df)

# Save the result to stg_products.csv
renamed_df.to_csv('stg_products.csv', index=False)

print("Data has been saved to stg_products.csv successfully.")
