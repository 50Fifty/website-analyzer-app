import json

def NewInvalidOperationError():
    return json.dumps({
        'error': 'invalid operation'
    })