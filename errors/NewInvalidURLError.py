import json

def NewInvalidURLError():
    return json.dumps({
        'error': 'invalid url'
    })