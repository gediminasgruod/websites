# Finance Tracker App

Finance Tracker App is a web application that allows users to track stock market data for a given stock symbol. It retrieves stock data from the Alpha Vantage API and provides a user-friendly interface to display the stock's historical data and calculate the daily return.

## Features

- Retrieve stock data using the Alpha Vantage API.
- Display historical stock data including open, high, low, close, and volume.
- Calculate and display the daily return for each day's stock data.

## Technologies Used

- Python
- Flask (a micro web framework for Python)
- Alpha Vantage API

## Prerequisites

Before running the app, make sure you have the following installed:

- Python 3.x
- Flask library (`pip install flask`)
- Requests library (`pip install requests`)

## Installation

1. Clone the repository:

git clone <repository_url>

2. Navigate to the project folder:

cd finance-tracker-app

3. Install the required dependencies:

pip install -r requirements.txt

## Usage

1. Obtain an API key from the Alpha Vantage website by signing up for an account.

2. In the `stock_data_retriever.py` file, replace the value of the `api_key` variable with your actual API key.

3. Run the Flask app:

flask run

4. Open a web browser and go to `http://localhost:5000` to access the app.

5. Enter a stock symbol in the input field and click the "Submit" button.

6. The app will retrieve the stock data and display it in a table on the page, including the calculated daily return.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request to this repository.
