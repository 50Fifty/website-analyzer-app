import json

def NewInvalidMessageError():
    return json.dumps({
        'error': 'invalid message'
    })   