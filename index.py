from flask import Flask, request, jsonify
import sys
sys.path.insert(1, 'modules')
from flask_cors import CORS
from createSummarizer import createSummarizer
from modules.app import *



# Start app
app = Flask(__name__)
CORS(app)

print("Testing")


mod = getModules()
print("getModules()::",mod)


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



allFunction = []
for module in getModules():
    # print(module.keys())
    for mod in module.keys():
        # print(mod)
        for func in module[mod]:
            # print(func[1].__name__)
            allFunction.append(func)


@app.route(endpoint + '/custom-function', methods=['GET','POST'])
def customFunction():
    if request.method == 'POST':
        routeCalled = request.args.get('routeCalled')
        prompt = request.args.get('prompt')
        print(routeCalled)
        for func in allFunction:
            if func[0] == routeCalled:
                print(func[1])
                return func[1](prompt)

        # return jsonify({"data": "data"}), 200

            



            

# Start app on http://127.0.0.1:5000/api/v1
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)