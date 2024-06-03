import requests

def download_csv_from_github(raw_url, output_path):
    """
    Downloads a CSV file from a GitHub repository.
    """
    # Send a GET request to the raw URL
    response = requests.get(raw_url)
    
    # Raise an exception if the request was not successful
    response.raise_for_status()
    
    # Write the content to the output file
    with open(output_path, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded successfully and saved to {output_path}")

# Example usage
raw_url = 'https://github.com/smjohnsonShipyard/GitHub-demos/blob/main/demo_data/raw_customers.csv'
output_path = 'raw_customers.csv'

download_csv_from_github(raw_url, output_path)
