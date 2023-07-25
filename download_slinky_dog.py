import requests

url = 'https://cdn.touringplans.com/datasets/slinky_dog.csv'
response = requests.get(url)

# ensure we got a valid response
if response.status_code == 200:
    # open in binary mode
    with open('slinky_dog_dash.csv', 'wb') as file:
        # write to file
        file.write(response.content)
else:
    print(f"Failed to get URL. Status code: {response.status_code}")
