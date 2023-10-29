import json

def NewMissingURLError(string:bool=True):
    error = {
        'error': 'missing url'
    }

    if string:
        return json.dumps(error)
    
    return error