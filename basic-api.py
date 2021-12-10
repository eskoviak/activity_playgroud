from crypt import methods
from flask import Flask, make_response, request, current_app
from flask_restful import Resource, Api
from functools import update_wrapper
from datetime import timedelta
from activity import Activty

## Server
app = Flask(__name__)
#api = Api(app)
activity = Activty()

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

## External Resources
class HelloWorld(Resource):
    def get(self):
        return {'id': '1234', 'name' : 'splendiferous'}

## Routes
#api.add_resource(HelloWorld, '/')
#api.add_resource(Categories, '/categories')        

@app.route('/', methods=['GET', 'OPTIONS'])
@crossdomain(origin="*", headers="*")
def hello():
    return {'id': '1234', 'name' : 'splendiferous'}

@app.route('/categories', methods=['GET','OPTIONS'])
@crossdomain(origin='*', headers='*')
def categories():
    category_dict = {}
    for item in activity.get_categories():
        category_dict[item.id] = item.category_name

    return category_dict

if __name__ == '__main__':
    app.run(debug=True, port=5100)
