from flask import Flask, Blueprint, request, jsonify
from mocks import categories as categories_mock

blueprint = Blueprint('categories', __name__, url_prefix='/categories')

# url_for('create_category') builds correct path


# @blueprint.route('/')
# def hello_world():
#     return 'Hello, World!'


@blueprint.route('/new', methods=['POST'])
def create_category():
    return 'Create category'

# dict will be converted to JSON automatically
# for other ones use jsonify() or use community extensions
@blueprint.route('/<uuid:category_id>', methods=['GET'])
def get_category(category_id):
    res = categories_mock.getCategoryById(str(category_id))
    return res


@blueprint.route('/<uuid:category_id>', methods=['PATCH'])
def update_category(category_id):
    return 'Update category %s' % category_id


@blueprint.route('/', methods=['GET'])
def get_categories():
    return jsonify(categories_mock.all_categories)
