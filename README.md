# Real-time Crypto Price Tracker 📈

This project is an automated ETL pipeline that tracks and records the market data for top cryptocurrencies over time. It's designed to run automatically, creating a historical dataset of price fluctuations.

The system fetches live data from the CoinGecko API, processes it using Python and pandas, and appends the new data to a master CSV file. The entire process is automated to run hourly using **GitHub Actions**, making this a self-updating data project.

---

## 🚀 Core Features

- **Automated ETL Pipeline:** A complete Extract, Transform, and Load process.
- **Historical Data Logging:** Instead of creating new files, the script intelligently appends new data to a master file (`crypto_prices_master.csv`), building a valuable time-series dataset.
- **Scheduled Execution:** The pipeline is configured with **GitHub Actions** to run automatically every hour, ensuring the dataset is always up-to-date.
- **Robust & Scalable:** The code is structured for clarity and handles data merging efficiently.

---

## 🛠️ Technologies & Architecture

- **Language:** Python 3
- **Core Libraries:**
    - `requests`: For making HTTP requests to the CoinGecko API.
    - `pandas`: For all data manipulation, processing, and CSV operations.
- **Automation & CI/CD:**
    - `GitHub Actions`: For scheduling and automating the entire ETL workflow on the cloud.
- **Workflow:**
    1.  **Extract:** A GET request is sent to the CoinGecko API to fetch the latest market data.
    2.  **Transform:** The raw JSON response is cleaned, structured, and loaded into a pandas DataFrame. A UTC timestamp is added to each record.
    3.  **Load & Append:** The script reads the existing `crypto_prices_master.csv`, appends the new DataFrame to it, and saves the combined data back to the file.
    4.  **Automate:** This entire process is triggered hourly by a scheduled GitHub Actions workflow, which then commits the updated data file back to the repository.

---

## 📊 The Dataset

The output is a single CSV file, `crypto_prices_master.csv`, with the following columns:

| Column              | Description                                      |
| ------------------- | ------------------------------------------------ |
| `name`              | The full name of the cryptocurrency.             |
| `symbol`            | The ticker symbol (e.g., BTC, ETH).              |
| `current_price_usd` | The current price in US Dollars.                 |
| `market_cap`        | The total market capitalization.                 |
| `total_volume`      | The total trading volume in the last 24 hours.   |
| `price_change_24h`  | The price change percentage in the last 24 hours.|
| `timestamp_utc`     | The UTC timestamp when the data was fetched.     |

---

## 🏁 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Amr-Walid/crypto-price-analyzer.git
    cd crypto-price-analyzer
    ```
2.  **Create and activate a virtual environment (recommended ):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the script:**
    ```bash
    python main.py
    ```
    This will either create `crypto_prices_master.csv` or append new data to it if it already exists.

---

## 🤖 Automation with GitHub Actions

This repository is configured to update itself automatically. You can view the execution history and logs under the **[Actions tab](https://github.com/Amr-Walid/crypto-price-analyzer/actions )** of this repository. The workflow runs on an hourly schedule.
