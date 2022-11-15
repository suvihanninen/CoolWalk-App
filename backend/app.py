import json
from flask import Flask, request, redirect

from optimal_path_service import compute_optimal_path

app = Flask(__name__)
app.config["DEBUG"] = True

"@app.route("/")"
"def home():"
"return hello"

@app.route('/coolwalk/optimal_path/<fr>/<to>', methods=['GET', 'POST'])
def distance(fr, to):

    # show the user profile for that user
    result = compute_optimal_path(fr, to)
    return result

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True, port=5000)