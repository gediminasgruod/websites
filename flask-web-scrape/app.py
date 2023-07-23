from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__, static_url_path='/static')

# List of bad words to exclude from word analysis
bad_words = set(["the", "a", "in", "of", "to", "you", "and", "at", "on", "for", "from", "is", "that", "his",
                 "are", "be", "-", "as", "&", "they", "with", "how", "was", "her", "him", "i", "has", "|", "an",
                 "string", "this", "if"])

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form['url']

    # Fetch website content using requests
    response = requests.get(url)
    if response.status_code != 200:
        return "Error: Invalid URL or Website Unreachable."

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    # Preprocess text (remove unwanted characters, stopwords, etc.)
    # Add your text preprocessing code here (not shown in this example)

    # Count word occurrences and filter out bad words
    words = [word for word in text.split() if word.lower() not in bad_words]
    word_freq = Counter(words)

    # Get the top 10 words and their frequencies
    top_words = dict(word_freq.most_common(10))

    # Generate a bar plot
    plt.bar(top_words.keys(), top_words.values())
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 10 Words')
    plt.xticks(rotation=45)

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('results.html', url=url, top_words=top_words, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
