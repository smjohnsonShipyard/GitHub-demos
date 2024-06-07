import pandas as pd

# Read the raw_orders.csv file
source_df = pd.read_csv('raw_orders.csv')

# Rename the columns as specified
renamed_df = source_df.rename(columns={
    'id': 'order_id',
    'store_id': 'location_id',
    'subtotal': 'subtotal_cents',
    'tax_paid': 'tax_paid_cents',
    'order_total': 'order_total_cents'
})

# Select the desired columns
renamed_df = renamed_df[[
    'order_id',
    'location_id',
    'customer_id',
    'subtotal_cents',
    'tax_paid_cents',
    'order_total_cents',
    'ordered_at'
]]

# Display the final DataFrame
print(renamed_df)

# Optionally, save the result to a CSV file
renamed_df.to_csv('stg_orders.csv', index=False)

print("Data has been saved to stg_orders.csv successfully.")
