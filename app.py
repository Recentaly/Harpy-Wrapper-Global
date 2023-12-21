# import modules for local server
from flask import Flask, request, Response, jsonify
from flask_cors import CORS

# import the api
from modules.api import Api

# other modules
from modules.response.parse_model_name import parse_model_name

# import modules for conversion to openai format
from modules.format.openai_generic import get_openai_generic

# import modules for openai streaming
from modules.format.openai_streamed import get_openai_streamed, get_streamed_last

# typing
from modules.typing import Output

# time module for slight delay
from time import sleep

# import module to read yaml files
import yaml

# read the config file
with open('modules/config.yaml', 'r') as file:

    # load the config file
    config = yaml.load(file, Loader=yaml.FullLoader)
    AUTH_KEY: str = str(config['AUTH_KEY'])

# create a new flask app
app = Flask(__name__)

# enable cors
CORS(app)

# create an instance of the api
Api = Api(url='https://api.harpy.chat/llm/harpyai/huggingface', auth=AUTH_KEY)

# generation routes
@app.route('/chat/completions', methods=['POST'])
def chat_completions():

    # get the data from the request
    data = request.get_json(force=True)

    # print debug
    #print(f"Model: {data['model']}\nMessages: {data['messages']}\nTemperature: {data['temperature']}\nMax Tokens: {data['max_tokens']}\nStream: {data['stream']}")

    # streaming here gets a full response but gradually returns each token for a 'beautiful' effect
    def beautiful_stream():

        # generate the response
        response = Api.generate(
            messages=data['messages'],
            settings={
                "temperature": data['temperature'],
                "max_new_token": data['max_tokens'],
                "model": f"{parse_model_name(data['model'])}"
            }
        )

        # split each words in the response and token into a list but add a space in between words
        response = response.split(' ')

        # now, gradually return each token
        for token in response:

            print(f"The token is: {token}")

            # yield the encoded token in OpenAI format
            yield b'data: ' + str(get_openai_streamed(content=token)).encode(encoding='utf-8') + b'\n\n'
            sleep(0.05)

        # at the very end, yield the last chunk which contains the 'stop' finish reason
        yield b'data: ' + str(get_streamed_last()).encode(encoding='utf-8') + b'\n\n'

        # and then signal end
        yield b'data: [DONE]'

    # check if user wants a streamed response or not
    if not data['stream']:

        # generate the response
        ai_response: Output = Api.generate(
            messages=data['messages'],
            settings={
                "temperature": data['temperature'],
                "max_new_token": data['max_tokens'],
                "model": f"{parse_model_name(data['model'])}"
            }
        )

        # craft a response
        response = jsonify(

            get_openai_generic(
                model=data['model'],
                content=ai_response,
            )
        ), 200

        # return the response
        return response

    # if not, we send a streamed one back
    else:

        return Response(beautiful_stream(), mimetype='text/event-stream')

# this route returns a list of the models
@app.route('/models', methods=['GET', 'OPTIONS'])
def models():

    return jsonify(
        {"data": [
            {"id": "sparrow-beta (ignore this: gpt)"},
         ]
        }
    ), 200

# root route (moistly to check if the server started correctly)
@app.route('/')
def index():

    return '<h2>Your link works!</h2>'

# run the server
if __name__ == '__main__':

    app.run(debug=False, port=5000)
