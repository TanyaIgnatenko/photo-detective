from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify, json
import base64
from check_image import is_modified
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/check', methods=['POST'])
def check():
    if request.method == 'POST':
        b64data = json.loads(request.data)['image']
        b64data = b64data.split('base64,', maxsplit=1)[1]
        image = base64.b64decode(b64data)
#         modified = is_modified(image)
        modified = True
        if modified:
            status = 'modified'
        else:
            status = 'original'

    return jsonify(status=status)

