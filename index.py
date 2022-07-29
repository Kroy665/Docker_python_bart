from flask import Flask, request, jsonify
from flask_cors import CORS
from createSummarizer import createSummarizer

# Start app
app = Flask(__name__)
CORS(app)

print("Testing")
endpoint = '/api/v1'

# http://127.0.0.1:5000/api/v1/create-summarize
@app.route(endpoint + '/create-summarize', methods=['GET','POST'])
def get_function():
    if request.method == 'GET': 

        print(request)
        
        # whatever you wanne do
        s = {"value": "data"}
        return jsonify(s), 200

    
    if request.method == 'POST': 
        request_data = request.get_json()
        print(request_data)
        
        # whatever you wanne do
        if request_data['text']:
            res = createSummarizer(request_data['text'])


        s = {"data": res}
        return jsonify(s), 200


# Start app on http://127.0.0.1:5000/api/v1
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)