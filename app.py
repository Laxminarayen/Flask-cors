from flask import Flask
from flask_cors import CORS
from flask import make_response
from OpenSSL import SSL
import ssl
import json
app = Flask(__name__)
CORS(app)

lang = 'English'
fs = 22050

@app.route('/')
def index():
    data = {"snd": "Flask return from ec2"}
    res = app.response_class(response=json.dumps(data),
                             status=200,
                             mimetype='application/json',
                             headers={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': '*',
        # 'Access-Control-Allow-Credentials' : true,
        'Content-Type': 'application/json'
    })
    # print(data)
    # print(res )

    return res

if __name__ == ('__main__'):
    app.run(host='0.0.0.0', port=8080)
