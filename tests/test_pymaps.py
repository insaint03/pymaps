from pymaps import maps, filters, reduces
from unittest import TestCase

class TestMaps(TestCase) :
    def test_maps(self):
        @maps
        def mods(x:int, mod:int=3) -> int :
            return x % mod
        
        actual = tuple(mods(1,2,3,4,5))
        expects = (1,2,0,1,2)

        self.assertEqual(actual, expects)
    
    def test_filters(self):
        @filters
        def odds(x:int) -> bool :
            return x % 2 == 1
        
        actual = tuple(odds(1,2,3,4,5))
        expects = (1,3,5)

        self.assertEqual(len(actual), len(expects))
        for (i, ex) in enumerate(zip(actual, expects)) :
            (a,e) = ex
            self.assertEqual(a, e, f'index {i} failed')

    def test_reduces(self):
        @reduces(0)
        def sum(total:int, x:int) -> int :
            return total + x
        
        actual = sum(1,2,3,4,5)
        expects = 15

        self.assertEqual(actual, expects)

