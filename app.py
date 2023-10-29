from flask import Flask, request
from services import WhoIsService
import json
from flask_sockets import Sockets
import uuid
from validators import validate_url
from errors import NewInvalidMessageError, NewInvalidURLError, NewInvalidOperationError, NewSessionNotFoundError, NewInvalidJSONError, NewMissingURLError

app = Flask(__name__)
sockets = Sockets(app)
ws_clients = dict()
info_services = dict()

@app.route('/', methods=['GET'])
def analyse_handler():
    request_data = request.args
    
    if 'url' not in request_data:
        return NewMissingURLError(string=False), 400

    url = request_data['url']
    
    if not validate_url(url):
        return NewInvalidURLError(string=False), 400

    info_service = WhoIsService(url)

    return {
        'info' : info_service.get_info(),
        'subdomains' : info_service.get_subdomains(),
        'asset_domains' : info_service.get_asset_domains()
    }

@sockets.route('/ws')
def analyse_websocke(ws):
    client_id = str(uuid.uuid4())
    ws_clients[client_id] = dict()

    while not ws.closed:
        message = ws.receive()
        if message:
            try:
                data = json.loads(message)
            except:
                ws.send(NewInvalidJSONError())
            else: # only executes if no exception is raised
                if 'url' in data:

                    if not validate_url(data['url']):
                        ws.send(NewInvalidURLError())
                    else:
                        ws.send(json.dumps({"data": f"creating session for {data['url']}..."}))
                        ws_clients[client_id]['url'] = data['url']
                        info_services[client_id] = WhoIsService(data['url'])
                        ws.send(json.dumps({"data": f"session created for {data['url']}"}))

                elif 'operation' in data:
                    if 'url' not in ws_clients[client_id]:
                        ws.send(NewSessionNotFoundError())

                    elif data['operation'] == 'get_info':
                        ws.send(json.dumps({"data": info_services[client_id].get_info()}))

                    elif data['operation'] == 'get_subdomains':
                        ws.send(json.dumps({"data": info_services[client_id].get_subdomains()}))
                    
                    elif data['operation'] == 'get_asset_domains':
                        ws.send(json.dumps({"data": info_services[client_id].get_asset_domains()}))
                    else:
                        ws.send(NewInvalidOperationError())
                else:
                    ws.send(NewInvalidMessageError())
        else:
            ws.send(NewInvalidMessageError())

if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()