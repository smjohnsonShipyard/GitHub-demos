import argparse
import os
import pandas as pd
from simple_salesforce import Salesforce

username = 'blake@shipyardapp.com'
password = os.environ.get('sf_password')
security_token = os.environ.get('sf_token')
query = 'SELECT FIELDS(ALL) from contact LIMIT 200'
destination_file_name = 'salesforce.csv'

sf_connection = Salesforce(
username=username,
password=password,
security_token=security_token,
client_id='Shipyard')

sf_data = sf_connection.query_all(query)
sf_df = pd.DataFrame(sf_data['records']).drop(columns='attributes')
sf_df.to_csv(destination_file_name, index=False)
print(f'Successfully stored results to {destination_file_name}')
