from flask import Flask
from flask import jsonify
from flask import request

from convert import *

app = Flask(__name__)
converter = CidrMaskConverter()
validate = IpValidate()

# Just a health check
@app.route("/")
def url_root():
    return "OK"

# Just a health check
@app.route("/_health")
def url_health():
    return "OK"

@app.route("/cidr-to-mask")
def url_cidr_to_mask():
    val = request.args.get('value')
    res = {
        "function": "cidrToMask",
        "input": val,
        "output": converter.cidr_to_mask(val),
    }
    return jsonify(res)

@app.route("/mask-to-cidr")
def url_mask_to_cidr():
    val = request.args.get('value')
    res = {
        "function": "maskToCidr",
        "input": val,
        "output": converter.mask_to_cidr(val),
    }
    return jsonify(res)

@app.route("/ip-validation")
def url_ipv4_validation():
    val = request.args.get('value')
    res = {
        "function": "ipv4Validation",
        "input": val,
        "output": validate.ipv4_validation(val),
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
