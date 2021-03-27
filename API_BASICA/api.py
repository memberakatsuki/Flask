from flask import Flask,jsonify
import json

app = Flask(__name__)

content = open('quotes.json','r')
load_content = json.load(content)

@app.route('/',methods=['GET'])
def pageOne():
    return ('1 - add /quotes(will return the complete list)|'
            '2 - add /quotes/id(where the "id" will be the index of the list you choose)|'
            '3 - add /quotes/legth(this page will count how many elements are in that list)')


@app.route('/quotes',methods=['GET'])
def index():
    return jsonify(load_content)

@app.route('/quotes/<id>')
def SearchForID(id):
    list_content = [load_content]
    for i in list_content:
        return jsonify(i[int(id)])

@app.route('/quotes/lenght')
def TotalCitations():
    list_content = [load_content]
    for e in list_content:
        cont = len(e)
    return f'Há {cont} citações registradas no arquivo quotes.json'

if __name__ == '__main__':
    app.run(debug=True)
