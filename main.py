import requests 
import pandas as pd
from datetime import datetime
import os
def fetch_crypto_data():
    """Fetches cryptocurrency data from the CoinGecko API."""
    print("Fetching data from CoinGecko API...")
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=5&page=1&sparkline=false"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("Data fetched successfully!")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data : {e}")
        return None
def process_data (raw_data):
    if not raw_data:
        print("No data to process")
        return None
    print("Processing data")
    processed = []
    for i in raw_data:
        processed.append({
                          'name': i.get('name'),
                          'symbol' : i.get('symbol'),
                          'current_price_usd': i.get('current_price'),
                          'market_cap': i.get('market_cap'),
                          'total_volume': i.get('total_volume'),
                          'price_change_24h': i.get('price_change_percentage_24h')
                          })
    new_df = pd.DataFrame(processed)
    print("Data processed into DataFrame")
    return new_df
def save_or_merge_data_to_csv (new_df) :
    """
    Saves the DataFrame to a CSV file. If the file already exists,
    it merges the new data with the old data.
    """
    if new_df is None or new_df.empty:
        print ("The new file is Empyty")
        return
    filename = "crypto_prices.csv"
    print (f"preparing to save data in {filename}")
    new_df['timestamputc'] = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    try:
        if os.path.exists(filename):
            old_df = pd.read_csv(filename)
            concat_df = pd.concat([old_df,new_df],ignore_index=True)
            print(f"Appending new data. Total rows in file: {len(concat_df)}")
            concat_df.to_csv(filename,index=False)
        else:
            print("file dose not exist .. creating new file")
            new_df.to_csv(filename,index=False)
        print("data saved sucssefully")
    except Exception as e:
        print("there is an error")
if __name__ == "__main__" :
     print("crypto_Analyzer is running")
     raw_data = fetch_crypto_data()
     process_data_df = process_data(raw_data)
     save_or_merge_data_to_csv(process_data_df)
     print("process finised")
     