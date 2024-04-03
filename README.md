# Yet to make simpler map/reduce syntax for python

Comparing javascript map/reduce, python functools.map/reduce feature rather mass up its clearity.

```javascript
// try to sum up even numbers multiply by their order, from 1 to N
function proceed(N) {
    // assert 1<N
    assert(1<N && typeof(N) === 'number', `N ought to be >1 number but ${N}`)
    // shifting remove heading "0"
    let sequence = (new Array(N)).map((_,i)=>i).filter((x)=>0<x); 
    // run,
    return sequence
        .filter((x)=>x%2===0)         // filter even numbers
        .map((x,i)=>x*(i+1))          // value * order
        .reduce((sum, x)=>sum+x, 0)   // sum up total
}
```

will be multi-level nested functions like:

```python
def proceed(N:int) :
    assert 1<N and isinstance(N, int), f'N ought to be >1 int but {N}'
    # ranging is simpler, though.
    sequence = range(1, N)
    # sum up totals, of
    return functools.reduce(lambda sum,x: sum+x
        # value * order, of
        , map(lambda i,x: x*(i+1)
            # filtered even numbers
            , enumerate(filter(lambda x: x%2===0, sequence))
        )
    )
```

## Alternative

The goal of this package is to make it simpler. Say at least -

```python

def proceed(N:int) :
    assert 1<N and isinstance(N, int), f'N ought to be >1 int but {N}'
    # ranging is simpler, though.
    sequence = range(1, N)
    
    # decorator annotates processes
    _filter = @filters(lambda x: x%2 === 0)

    # then do maps
    @maps
    def _maps(X): 
        (i,x) = X
        return x*(i+1)
    
    # finally, reduces
    @reduces(init=0)
    def _total(agg, x) : return agg+x
    
    # now get it run
    return applies(_filter, _maps, _total)(*sequence)

```

- [x] map
- [x] filter
- [x] reduce
- [ ] applies

## Further benefits

- [ ] advant multiprocessing


    