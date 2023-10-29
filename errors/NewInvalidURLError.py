import json

def NewInvalidURLError(string:bool=True):
    error = {
        'error': 'invalid url'
    }

    if string:
        return json.dumps(error)
    
    return error