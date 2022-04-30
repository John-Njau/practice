from flask import render_template
from app import app
from .requests import news_articles, get_sources


@app.route('/')
def index():
    index = "index.html"
    title = "Home Page"
    sources = get_sources()
    return render_template(index, title=title, sources=sources)


@app.route('/articles/<id>')
def articles(id):
    title= "Flask catchUp"
    articles = "articles.html"
    n_aricles = news_articles(id)
    return render_template(articles, title=title, articles = n_aricles)
    

@app.route('/about')
def about():
    return render_template("about.html")
