import json

def NewInvalidMessageError(string:bool=True):
    error = {
        'error': 'invalid message'
    }

    if string:
        return json.dumps(error)
    
    return error