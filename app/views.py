from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_news,search_news
from .models import review
from .forms import ReviewForm

REview = review.Review

#views
@app.route('/news/<int:id>')
def index(id):

    '''
    view news page function that returns the news details  and its data
    '''
    #Getting latest news
    news = get_news(id)
    trending_news = get_news('trending')
    sports_news = get_news('sports')
    business_news = get_news('business')
    print(trending_news)
    news =get_news(id)
    title = f'{news.title}'
    reviews = Review.get_reviews(news.id)
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, trending = trending_news, sports = sports_news, business = business_news )
    return render_template('news.html', id = news_id, title = title, news = news, reviews = reviews)

@app.route('/search/<news_name>')
def search(news_name):
'''
    View function to display the search results
    '''
    news_name_list = movie_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)

@app.route('/news/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    news = get_news(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.id,title,news.poster,review)
        new_review.save_review()
        return redirect(url_for('news',id = news.id ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)