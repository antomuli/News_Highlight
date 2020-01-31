from flask import render_template
from app import app

#views
@app.route('/news/<news.id>')
def news(news_id):

    '''
    view news page function that returns the news details  and its data
    '''
    title = 'Home - Welcome to the updated news_highlight website'
    return render_template('news.html', id = news_id, title = title)