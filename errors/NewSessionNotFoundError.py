import json

def NewSessionNotFoundError():
    return json.dumps({
        'error': 'session not found'
    })