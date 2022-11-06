from app import app
from flask import render_template, redirect ,request
from models import *
from forms import Form_add_category, Form_add_news


@app.route('/', methods=['GET', 'POST'])
def index():
    new = News.select().join(Category)
    list_new = []
    for n in new:
       list_new.append([n.text,n.category_id.name])
       print('----' * 5)
       print(n.text)
       print(n.category_id.name)
    return render_template('index.html',list_new=list_new)

@app.route('/form_category', methods=['GET', 'POST'])
def form_category():
    form = Form_add_category()
    return render_template('form_category.html', form = form)

@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    form = Form_add_category()
    if form.validate_on_submit():
        Category(name = form.textf.data).save()
        return redirect('/')
    return render_template('index.html')


@app.route('/form_news', methods=['GET', 'POST'])
def form_news():
    form = Form_add_news()
    return render_template('form_news.html', form = form)

@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    form = Form_add_news()
    if form.validate_on_submit():
        News(name = form.name.data,
             text = form.textf.data,
             category_id = form.category_id.data
             ).save()
        return redirect('/')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)