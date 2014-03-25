import unittest
import solution
import itertools

class TestAlternateGenerator(unittest.TestCase):
    def test_one_input(self):
        alternative_count = solution.alternate(lambda: \
                            itertools.chain([1, 3],
                            itertools.count(0,-2)))
        solution_count = [next(alternative_count) for i in range(10)] 
        self.assertEqual(solution_count, [1, 3, 0, -2, -4, -6, -8, -10, -12, -14]) 
    
    def test_no_parameters_passed(self):
        alternative_count = solution.alternate()
        self.assertRaises(StopIteration, next, alternative_count)

if __name__ == '__main__':
    unittest.main()  
