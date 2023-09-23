from flask import Flask, request, Response
from cohere_interface import generate
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@cross_origin
@app.route("/cohere-generate/<message>", methods=['GET'])
def cohereGenerate(message):
    try:
        # prompt = request.get_data(as_text=True)
        result = generate.generateResponse(message)
        return Response(result, status=200) 
    except Exception as e:
        print(e)
        return Response(status=400)


@cross_origin
@app.route("/hello", methods=['GET'])
def hello():
    return ''