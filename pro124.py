import json
from flask import Flask, jsonify, request

app= Flask(__name__)

@app.route('/')

def flask1():
    return('there is something')

@app.route('/flask')

def flask2():
    return('here also something')

tasks= [
    {
        'id':1,
        'contact':'8759075897',
        'name':'Raj',
        'done': False
    }
]

@app.route('/data', methods=['get'])
def data():
    return(jsonify({'task': tasks}))


@app.route('/add-data', methods=['post'])
def add():
    task={
        'id': tasks[-1]['id'] +1,
        'contact': request.json['contact'],
        'name': request.json['name'],
        'done': False
        }

    tasks.append(task)
    return(jsonify({'task': tasks}))


app.run(debug=True)