import json

def NewInvalidOperationError(string:bool=True):
    error = {
        'error': 'invalid operation'
    }

    if string:
        return json.dumps(error)

    return error