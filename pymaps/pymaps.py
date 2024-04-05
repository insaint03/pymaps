from functools import reduce

'''
    apply added. v0.1.0.20240405
'''

def maps(fn:callable, **options) :
    ''' 
        maps decorator, map *args with fn(args, **kwargs) 
    '''
    def _wrap(*args, **kwargs) :
        return map(lambda x: fn(x, **kwargs), args)
    # revoke original function name & signature
    _wrap.__name__ = fn.__name__
    _wrap.__annotations__ = fn.__annotations__
    return _wrap

def filters(fn:callable, **options) :
    '''
        filters decorator, filter *args with fn(args, **kwargs)
    '''
    def _wrap(*args, **kwargs) :
        return filter(lambda x: fn(x, **kwargs), args)
    # revoke original function name & signature
    _wrap.__name__ = fn.__name__
    _wrap.__annotations__ = fn.__annotations__
    return _wrap

def reduces(init, **options) :
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


def apply(*fns:callable, **options):
    ''' sequencial runner; step a process then pass to next '''
    def _wrap(*values) :
        cursor = values
        for fn in fns :
            cursor = fn(*cursor, **options)
        return cursor
    return _wrap


        

    