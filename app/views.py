from flask import render_template
from app import app

#views
@app.route('/news/<news.id>')
def news(news_id):

    '''
    view news page function that returns the news details  and its data
    '''
    return render_template('news.html', id = news_id)