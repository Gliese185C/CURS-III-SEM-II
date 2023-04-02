from flask import Flask, request, Response, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    guid = request.args.get('guid')
    data = request.get_json()
    print(data)
    print(guid)

    with open('data.json') as f:
        db = json.load(f)
    for object in db['users']:
        if object['id'] == guid:
            object['name'] = data['name']
            object['nick_name'] = data['userName']
            object['phone'] = data['phone']
            object['address'] = data['address']
            object['pass id'] = data['pass_id']
            f.close()
            with open('data.json','w') as f:
                json.dump(db,f,indent=4)
            return {
                'process': True,
                'content': ''
             }
    return {
        'process': False,
        'content': ''
    }

@app.route('/get_data_guid', methods=['GET'])
def get_data_guid():
    guid = request.args.get('guid')
    with open('data.json') as f:
        data = json.load(f)
    for object in data['users']:
        if object['id'] == guid:
            return {'process':True,
                    'content':object}
    return {
        'process': False,
        'content': ''
    }

@app.route('/get_head', methods=['HEAD'])
def get_head():
    current_time_micro = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    headers = {'time': current_time_micro}
    return Response('', headers=headers)

@app.route('/get_options', methods=['OPTIONS'])
def get_options():
    response = jsonify({
        'message': 'This is an OPTIONS request!',
        'allowed_methods': ['GET', 'POST', 'PUT', 'DELETE']
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'OPTIONS,HEAD,GET,POST,PUT,DELETE')
    return response

if __name__ == '__main__':
    app.run(port=5000)
    #http://localhost:5000/
