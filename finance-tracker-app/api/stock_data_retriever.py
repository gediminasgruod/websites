import requests
import json

# Alpha Vantage API endpoint
url = "https://www.alphavantage.co/query"

# API key (replace 'YOUR_API_KEY' with your actual API key)
api_key = #YOUR_API_KEY

# Function to fetch stock data
def fetch_stock_data(symbol):
    # API parameters
    function = "TIME_SERIES_DAILY"  # Example function for daily stock data
    outputsize = "compact"  # Example output size, compact or full
    datatype = "json"  # Example data format, json or csv

    # Construct the API request URL
    params = {
        "function": function,
        "symbol": symbol,
        "outputsize": outputsize,
        "datatype": datatype,
        "apikey": api_key,
    }

    try:
        # Send the API request
        response = requests.get(url, params=params)

        # Parse the JSON response
        data = json.loads(response.text)

        # Extract the stock data from the response
        stock_data = []
        for date, info in data["Time Series (Daily)"].items():
            open_price = info["1. open"]
            high_price = info["2. high"]
            low_price = info["3. low"]
            close_price = info["4. close"]
            volume = info["5. volume"]

            # Calculate daily return
            prev_close = float(info["4. close"])
            if len(stock_data) > 0:
                prev_info = stock_data[-1]
                prev_close = float(prev_info["4. close"])

            daily_return = (float(close_price) - prev_close) / prev_close if prev_close != 0 else 0

            # Create a dictionary for each day's data
            day_data = {
                "date": date,
                "open": open_price,
                "high": high_price,
                "low": low_price,
                "close": close_price,
                "volume": volume,
                "daily_return": daily_return,
            }

            # Add the dictionary to the stock_data list
            stock_data.append(day_data)

        # Return the stock data
        return stock_data

    except requests.exceptions.RequestException as e:
        print("Error occurred during API request:", str(e))
