import json
from flask import Flask, request, redirect

# from optimal_path_service import compute_optimal_path

app = Flask(__name__)
app.config["DEBUG"] = True

# @app.route("/coolwalk")
# def home():
#    return "hello"

@app.route("/coolwalk", methods=['GET'])
def distance():
    fro = request.args.get("fro")
    to = request.args.get("to")
    print(f'language: {fro}, framework: {to}')
    featureObject = "{\"features\": [{\"geometry\": {\"coordinates\": [[-1.106321, 52.965347], [-1.106523, 52.966218], [-1.106675, 52.966204], [-1.107652, 52.966116], [-1.108331, 52.966054], [-1.108718, 52.966018], [-1.109553, 52.965944], [-1.109235, 52.964633], [-1.109036, 52.963744], [-1.109819, 52.963774], [-1.111205, 52.960773], [-1.111618, 52.959832], [-1.112093, 52.959586], [-1.112754, 52.959541], [-1.111552, 52.958683], [-1.111084, 52.958341], [-1.112433, 52.958242], [-1.112343, 52.957551], [-1.113667, 52.95569], [-1.117185, 52.957306], [-1.11785, 52.956792], [-1.118447, 52.956339], [-1.119196, 52.955868], [-1.120175, 52.955303], [-1.121231, 52.954768], [-1.121475, 52.954637], [-1.121796, 52.954469], [-1.122374, 52.954162], [-1.125264, 52.9559], [-1.127471, 52.954868], [-1.128914, 52.954259], [-1.129449, 52.954516], [-1.130158, 52.954847], [-1.130231, 52.954787], [-1.131038, 52.95323], [-1.131147, 52.952815], [-1.131195, 52.952631], [-1.131234, 52.95244], [-1.131293, 52.952192], [-1.131493, 52.95162], [-1.1321, 52.951886], [-1.132643, 52.950757], [-1.132934, 52.950819], [-1.133441, 52.950927], [-1.1343, 52.951113], [-1.135264, 52.951328], [-1.135515, 52.951375], [-1.135595, 52.951452], [-1.13626, 52.95139], [-1.137817, 52.95131], [-1.138469, 52.951263], [-1.139222, 52.950428], [-1.139419, 52.950414], [-1.140172, 52.950724], [-1.140234, 52.950861], [-1.140515, 52.951483], [-1.142295, 52.951119], [-1.142283, 52.95105], [-1.14376, 52.950882], [-1.145347, 52.951146], [-1.1459, 52.951345], [-1.146234, 52.951404], [-1.145907, 52.952117]], \"type\": \"LineString\"}, \"properties\": {}, \"type\": \"Feature\"}], \"type\": \"FeatureCollection\"}"


    # show the user profile for that user
    # result = compute_optimal_path(fr, to)
    return featureObject

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(host="0.0.0.0", debug=True, port=4000)