from flask import Flask, jsonify, request, json
from flask_restful import Resource, Api
from getKeyword import *
from getMatches import *
from luceneSearch import *
from luceneFunctionalities import *

app = Flask(__name__)

@app.route("/", methods=['GET'])
def func1():
    return jsonify ({"Hello": "World!"})

@app.route("/post", methods=['POST'])
def processRequest():
    requestFromServer = request.get_json()
    keyWord = findKeyword(requestFromServer['request'])
    finalKeyWord = removeArticle(keyWord).strip()
    ##Keyword found
    #Search corpus for keyword
    results = searchLucene(finalKeyWord)
    json_string = json.dumps([ob.__dict__ for ob in results])
    return json_string

if __name__ == '__main__':
    app.run(port=8080)