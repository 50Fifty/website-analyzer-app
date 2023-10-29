import json

def NewInvalidJSONError(string:bool=True):
    error = {
        'error': 'invalid json'
    }

    if string:
        return json.dumps(error)
    
    return error