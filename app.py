from flask import Flask, request, jsonify
from mocks import categories as categories_mock
app = Flask(__name__)

# url_for('create_category') builds correct path


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/categories/new', methods=['POST'])
def create_category():
    return 'Create category'

# dict will be converted to JSON automatically
# for other ones use jsonify() or use community extensions
@app.route('/categories/<uuid:category_id>', methods=['GET'])
def get_category(category_id):
    res = categories_mock.getCategoryById(str(category_id))
    return res


@app.route('/categories/<uuid:category_id>', methods=['PATCH'])
def update_category(category_id):
    return 'Update category %s' % category_id


@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories_mock.all_categories)
