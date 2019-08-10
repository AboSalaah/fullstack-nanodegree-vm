from flask import Flask , render_template
from sqlalchemy import create_engine
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item
app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def showCategoriesAndLatestitems():
    categories = session.query(Category)
    latestItems = session.query(Item).order_by(desc(Item.last_modification))
    return render_template('homepage.html',categories=categories, latestItems = latestItems)

@app.route('/catalog/<category_name>/items/')
def showCategoryItems(category_name):
    return ("these are %s items" %(category_name))

@app.route('/catalog/<category_name>/<string:item_name>/')
def showItemsDescription(category_name,item_name):
    return ("this is %s description of %s category" %(item_name,category_name))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)