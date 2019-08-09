from flask import Flask

app = Flask(__name__)

@app.route('/')
def showCategoriesAndLatestitems():
    return "the home page"

@app.route('/catalog/<category_name>/items/')
def showCategoryItems(category_name):
    return ("these are %s items" %(category_name))

@app.route('/catalog/<category_name>/<string:item_name>/')
def showItemsDescription(category_name,item_name):
    return ("this is %s description of %s category" %(item_name,category_name))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)