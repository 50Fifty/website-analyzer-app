from flask import Flask, request
import threading
from services import WhoIsService


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    request_data = request.args
    
    if 'url' not in request_data:
        return {
            'error': 'url is required'
        }, 400

    url = request_data['url']

    who_is_service = WhoIsService(url)

    results = who_is_service.resolve_all()

    isp = results['isp']
    org = results['org']
    asn = results['asn']

    return {
        'info' : {
            'ip': who_is_service.ip,
            'isp': isp,
            'organisation': org,
            'asn': asn
        }
        
    }

if __name__ == '__main__':
    app.run(debug=True)
