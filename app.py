import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
import pymongo

db_url = os.environ.get('DB_URL', 'mongodb://localhost:27017/')

app = Flask(__name__)

dbClient = MongoClient(db_url)
db = dbClient['SCORES']
collection = db['HIGH_SCORES']

@app.route('/high_scores', methods = ['GET', 'POST'])
def handle_high_scores():
  if request.method == 'GET':
    high_scores = []
    for document in collection.find().sort('score', pymongo.DESCENDING):
      record = {
        'score': document['score'],
        'name': document['name']
      }
      high_scores.append(record)
    return jsonify(high_scores)
    
  elif request.method == 'POST':
    record = {
      'score': request.json['score'],
      'name': request.json['name']
    }
    result = collection.insert_one(record)
    record['_id'] = str(result.inserted_id)
    return jsonify(record)

if __name__ == '__main__':
  app.run(debug=True)