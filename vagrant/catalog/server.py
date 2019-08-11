from flask import Flask , render_template
from sqlalchemy import create_engine
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

from flask import session as login_session
import random, string
import json
app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
CLIENT_ID = json.loads( open('credentials.json', 'r').read())['web']['client_id']
@app.route('/')
def showCategoriesAndLatestitems():
    categories = session.query(Category)
    latestItems = session.query(Item).order_by(desc(Item.last_modification))
    return render_template('homepage.html',categories=categories, latestItems = latestItems)

@app.route('/login')
def showLogin():
    #create anti-forgery state token
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return "The current session state is %s" % login_session['state']

@app.route('/catalog/<category_name>/items/')
def showCategoryItems(category_name):
    categories = session.query(Category)
    category = session.query(Category).filter_by(name = category_name).one()
    items = session.query(Item).filter_by(category_id = category.id)
    return render_template('category_items.html',categories=categories,items=items,category_name=category_name)
    

@app.route('/catalog/<category_name>/<string:item_name>/')
def showItemsDescription(category_name,item_name):
    category = session.query(Category).filter_by(name = category_name).one()
    item = session.query(Item).filter_by(category_id = category.id, name=item_name).one()
    return render_template('item_description.html',item = item)
    


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)