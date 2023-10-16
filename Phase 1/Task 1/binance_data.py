import requests
import pandas as pd

# Define the URL of the Binance API
url = 'https://api.binance.com/api/v3/ticker/24hr'

# Make an HTTP GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Create a DataFrame from the JSON data
    df = pd.DataFrame(data)

    # Specify the columns you want to keep in the CSV file
    columns_to_keep = ['symbol', 'lastPrice', 'volume', 'openPrice', 'highPrice', 'lowPrice']

    # Filter the DataFrame to keep only the specified columns
    df = df[columns_to_keep]

    # Save the DataFrame as a CSV file
    df.to_csv('binance_data.csv', index=False)

    print("CSV file 'binance_data.csv' created successfully.")
else:
    print("Failed to retrieve data from the API. Status code:", response.status_code)
