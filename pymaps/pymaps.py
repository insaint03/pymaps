from functools import reduce

'''
    very starts v0.0.1.20240403
'''

def maps(fn:callable) :
    ''' 
        maps decorator, map *args with fn(args, **kwargs) 
    '''
    def _wrap(*args, **kwargs) :
        return map(lambda x: fn(x, **kwargs), args)
    # revoke original function name & signature
    _wrap.__name__ = fn.__name__
    _wrap.__annotations__ = fn.__annotations__
    return _wrap

def filters(fn:callable) :
    '''
        filters decorator, filter *args with fn(args, **kwargs)
    '''
    def _wrap(*args, **kwargs) :
        return filter(lambda x: fn(x, **kwargs), args)
    # revoke original function name & signature
    _wrap.__name__ = fn.__name__
    _wrap.__annotations__ = fn.__annotations__
    return _wrap

def reduces(init) :
    '''
        reduces decorator, reduce *args with fn(agg, x, **kwargs)
    '''
    def _outer(fn:callable) :
        def _wrap(*args, **kwargs) :
            return reduce(lambda agg,x: fn(agg, x, **kwargs), args, init)
        # revoke original function name & signature
        _wrap.__name__ = fn.__name__
        _wrap.__annotations__ = fn.__annotations__
        return _wrap
    return _outer
    