import os
from flask import Flask, render_template, request
import feedparser

host = os.getenv('IP', '0.0.0.0')
port = int(os.getenv('PORT', 8080))

app = Flask(__name__)

# переменные хранят урлы для рсс
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
LENTA_TOP_FEED = "https://lenta.ru/rss/top7"

RSS_FEEDS = {
    'bbs': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640',
    'lenta' : "https://lenta.ru/rss/top7"
}



# @app.route("/")
# @app.route("/<publication>")
# def get_news(publication='lenta'):
#     feed = feedparser.parse(RSS_FEEDS[publication])
#     return render_template("index.html", articles=feed['entries'])

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "lenta"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("index.html", articles=feed["entries"])
    

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)

# 38