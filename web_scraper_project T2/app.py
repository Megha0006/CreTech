from flask import Flask, request, jsonify, render_template
from scraper import fetch_page, parse_page, save_to_csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    html = fetch_page(url)
    if not html:
        return jsonify({"error": "Failed to fetch URL"}), 500
    data = parse_page(html)
    if not data:
        return jsonify({"error": "No data found"}), 404
    save_to_csv(data)
    return jsonify({"message": "Scraping successful!", "data": data})

if __name__ == "__main__":
    app.run(debug=True)