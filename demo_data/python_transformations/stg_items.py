import pandas as pd

# Step 1: Read the source data
source_df = pd.read_csv('raw_items.csv')

# Step 2: Rename columns
renamed_df = source_df.rename(columns={
    'id': 'order_item_id',
    'sku': 'product_id'
})

# Select the desired columns to match the SQL script
renamed_df = renamed_df[['order_item_id', 'order_id', 'product_id']]

# Display the final DataFrame
print(renamed_df)

# Optionally, save the result to a CSV file
renamed_df.to_csv('stg_items.csv', index=False)
