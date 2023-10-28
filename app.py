from flask import Flask, request
import threading
from services import WhoIsInfoService


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    request_data = request.args
    
    if 'url' not in request_data:
        return {
            'error': 'url is required'
        }, 400

    url = request_data['url']
    url = url.strip()

    info_service = WhoIsInfoService(url)

    return {
        'info' : {
            'asn' : info_service.get_asn(),
            'isp' : info_service.get_isp(),
            'org' : info_service.get_org(),
            'location' : info_service.get_location(),
        },
        'subdomains' : info_service.get_subdomain(),
        'asset_domains' : info_service.get_asset_domains()
    }

if __name__ == '__main__':
    app.run(debug=True)