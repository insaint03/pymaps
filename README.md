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
    return apply(
        # ranging is simpler, though.
        filters(lambda x: x%2===0),
        # enumerate
        enumerate,
        # do maps
        maps(lambda i,x: x*(x+i)),
        # finally, reduce to the result
        reduces(total, x) : return total + x
    )
```

- [x] map
- [x] filter
- [x] reduce
- [x] apply

## Further benefits

- [ ] advance multiprocessing


    