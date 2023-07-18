from flask import Flask, render_template, request
from api.stock_data_retriever import fetch_stock_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symbol = request.form['symbol']
        stock_data = fetch_stock_data(symbol)
        return render_template('index.html', stock_data=stock_data, symbol=symbol)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
