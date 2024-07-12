def logged(fn):
    print('Adding logging to', fn.__name__)
    
    def wrapper(*args, **kwargs):
        print('Calling', fn.__name__)
        return fn(*args, **kwargs)
    
    return wrapper

