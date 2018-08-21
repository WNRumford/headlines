import os
from flask import Flask
import feedparser

host = os.getenv('IP', '0.0.0.0')
port = int(os.getenv('PORT', 8080))

app = Flask(__name__)

# переменные хранят урлы для рсс
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
LENTA_TOP_FEED = "https://lenta.ru/rss/top7"



@app.route("/")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    first_article = feed['entries'][0]
    return '''<html>
            <body>
                <h1> BBC Headlines </h1>
                <b>{0}</b></br>
                <i>{1}</i></br>
                <p>{2}</p></br>
            </body>
            </html>'''.format(first_article.get("title"),first_article.get("published"),
                                first_article.get("summary"))

# route for lenta.ru
@app.route("/lenta-top7")
def get_news_lenta():
    feed = feedparser.parse(LENTA_TOP_FEED)
    first_article = feed['entries'][0]
    return '''<html>
            <body>
                <h1> Lenta.ru Headlines </h1>
                <b>{0}</b></br>
                <i>{1}</i></b>
            </body>
            </html>'''.format(first_article.get("title"), first_article.get("description"))

    

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)