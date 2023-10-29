import json

def NewSessionNotFoundError(string:bool=True):
    error = {
        'error': 'session not found'
    }
    
    if string:
        return json.dumps(error)
    
    return error