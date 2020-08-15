from flask import Flask, request, jsonify, abort
# import requests
# import json
import db # db.py
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# i think more stuff can go here such as url string?? and we can embed env vars in here??
app.config['MONGODB_SETTINGS'] = {
    "db": "open_stata",
}

database = MongoEngine(app)

def returnError(errorCode, errorMsg):
    response = jsonify({ 'error': errorMsg })
    response.status_code = errorCode
    return response

@app.route('/users', methods=['GET', 'POST'])
def posts_route():
    if request.method == 'GET':
        return jsonify(db.getAllUsers())
    else:
        try:
            user = request.get_json()
            return jsonify(db.addUser(user))
        except:
            return returnError(400, 'user already exists')


# realistically we don't want to embed the username in here after we add some auth middleware
# that will hopefully auth with jwt and then embed username into request.username or something
@app.route('/user/<string:username>', methods=['GET', 'DELETE'])
def post_route(username):
    try:
        if request.method == 'GET':
            return jsonify(db.getUser(username))
        elif request.method == 'DELETE':
            return jsonify(db.deleteUser(username))
        # there isn't much to modify anyway for specifically a user
        # elif request.method == 'PUT':
        #     user = request.get_json()
        #     if user == None:
        #         return returnError(400, 'missing body')
        #     return jsonify(db.editUser(username, user))
    except:
        return returnError(404, 'user not found')

# same as above, hopefully we can reduce this to just a filename unique identifier
# and get rid of the username
# notably, we can't use filenames as unique identifiers and need to rely on the unique ids that mongo will generate
@app.route('/user/<string:username>/<string:filename>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def dofile_route(username, filename):
    return 'yay'

if __name__ == '__main__':
    app.run()
