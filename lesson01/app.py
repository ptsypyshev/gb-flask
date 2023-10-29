from flask import Flask
from flask import render_template
from lesson01.csv_load import load_dict, load_listdict, get_random_items, get_category_items

MAX_ITEMS_AT_MAIN = 6
CATEGORIES = load_dict('lesson01/categories.csv')
ITEMS = load_listdict('lesson01/items.csv')

app = Flask(__name__)

@app.route('/')
@app.route('/main/')
def html_index():
    context = {
        'title': 'Main page',
        'offers': CATEGORIES.values(),
        'items': get_random_items(ITEMS, MAX_ITEMS_AT_MAIN),
    }
    return render_template('main.html', **context)

@app.route('/category/<name>/')
def category(name=''):
    category = CATEGORIES.get(name)
    if category:
        context = {
            'category': {
                'name': name,
                'description': category['description'],
            },
            "items": get_category_items(ITEMS, name)
        }
        return render_template('category.html', **context)
    return render_template('not_found.html'), 404

if __name__ == '__main__':
    app.run()