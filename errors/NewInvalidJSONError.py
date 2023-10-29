import json

def NewInvalidJSONError():
    return json.dumps({
        'error': 'invalid json'
    })