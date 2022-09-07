from flask import Flask, request, jsonify
import sys
sys.path.insert(1, 'modules')
from flask_cors import CORS
from modules.getModules_app import *



# Start app
app = Flask(__name__)
CORS(app)

endpoint = '/api/v1'

allFunction = []
for module in getModules():
    # print(module.keys())
    for mod in module.keys():
        # print(mod)
        for func in module[mod]:
            print("Function Name::",func[1].__name__)
            allFunction.append(func)

# http://localhost:6000/api/v1/custom-function?routeCalled={Function_name}&prompt={prompt}
@app.route(endpoint + '/custom-function', methods=['GET','POST'])
def customFunction():
    if request.method == 'POST':
        routeCalled = request.args.get('routeCalled')
        prompt = request.args.get('prompt')
        print("routeCalled::",routeCalled)
        for func in allFunction:
            if func[0] == routeCalled:
                print(func[1])
                retureValue = func[1](prompt)
                print("retureValue::",retureValue)
                return retureValue
    else:
        return "Invalid request"
        
# Start app on http://127.0.0.1:5000/api/v1
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)