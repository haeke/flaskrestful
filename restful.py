from flask import Flask, jsonify, request
app = Flask(__name__)

#dict of languages
languages = [{ 'name': 'Javascript' }, { 'name': 'Python' }]

@app.route('/')
def index():
    return jsonify({ 'message': 'its working' })

#this route will list all of our languages
@app.route('/lang', methods=['GET'])
def listLanguages():
    return jsonify({ 'languages': languages })

#define routes for the different items in a dictionary
@app.route('/lang/<string:name>', methods=['GET'])
def listOne(name):
    #search a dictionary for any matches for 'name' in the languages dictionary
    langs = [language for language in languages if language['name'] == name]
    return jsonify( {'language': langs[0]})

#handle adding new JSON object to the language dictionary
@app.route('/lang', methods=['POST'])
def addOne():
    #use request.json to extract the data that being sent
    language = {'name' : request.json['name']}

    languages.append(language)
    return jsonify({'languages' : languages})


@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language': langs[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
