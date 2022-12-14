import OptimalPathService as optimalPathService
from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/coolwalk", methods=['GET'])
def get_optimal_path():
    fro = request.args.get("fro")
    to = request.args.get("to")
    geojson_feature_response = optimalPathService.OptimalPathService().compute_optimal_path(fro,to)
   
    return geojson_feature_response
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(host="0.0.0.0", debug=True, port=5000, threaded=True)

