import random

from flask import jsonify, request
from flask_cors import cross_origin
from app import app
from app.algorithm.ml import ml
from app.info import features, questions, answers, questionWithComplete

@app.route('/api/questions/', methods = ['POST'])
@cross_origin()
def getQuestions():
    availableFeatures = features[:]
    characterMatch = None

    if 'alreadyFeatures' in request.json:
        availableFeatures = set(availableFeatures) - set(request.json['alreadyFeatures'])
        characterMatch = ml(request.json['alreadyFeatures'], request.json['params'], request.json['answers'])
        characterMatch = characterMatch.to_dict()

        characterMatchId = 0
        for id in characterMatch['name']:
            characterMatchId = id

        print(characterMatch['name'][characterMatchId])

        characterMatch = {
          "name": characterMatch['name'][characterMatchId],
          "image": characterMatch['image'][characterMatchId],
          "eye_color": characterMatch['eye_color'][characterMatchId],
          "publisher": characterMatch['publisher'][characterMatchId],
          "place_of_birth": characterMatch['place_of_birth'][characterMatchId]
        }

    else:
        availableFeatures = set(availableFeatures) - set(questionWithComplete)

    availableFeatures = list(availableFeatures)

    if(not len(availableFeatures)):
        return jsonify(
            characterMatch = characterMatch
        )

    feature = random.choice(availableFeatures)
    param = feature
    question = questions[feature]

    if feature in questionWithComplete:
        question += characterMatch[feature]
        param = 'is_' + characterMatch[feature]

    return jsonify(
      feature = feature,
      param = param,
      question = question,
      answers = answers[feature],
      characterMatch = characterMatch
    )