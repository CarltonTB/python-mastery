from functools import wraps

def logformat(fmt: str):
    def logged(fn):
        print('Adding logging to', fn.__name__)

        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(fmt.format(fn=fn))
            return fn(*args, **kwargs)
        
        return wrapper

    return logged


logged = logformat(fmt='Calling {fn.__name__}')

