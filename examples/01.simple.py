from pymaps import maps, filters, reduces

'''
    Simple example of using pymaps:maps
    it will run as:
        mods(1,2,3,4,5) => (1,2,0,1,2)
    or may optional mod:int
        mods(1,2,3,4,5, mod=5) => (1,2,3,4,0)

'''
@maps
def mods(x:int, mod:int=3) -> int :
    return x % mod

'''
    Another for pymaps:filters
'''
@filters
def odds(x:int) -> bool :
    return x % 2 == 1

'''
    And pymaps:reduces
'''
@reduces(0)
def sum(total:int, x:int) -> int :
    return total + x

