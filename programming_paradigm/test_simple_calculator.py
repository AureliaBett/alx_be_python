import unittest
from simple_calculator import SimpleCalculator;

class Test_SimpleCalculator(unittest.TestCase):
    #add
    def test_add_positive(self):
        result = SimpleCalculator().add(5, 6)
        self.assertEqual(result, 11)
       
    def test_add_negative(self):
        result = SimpleCalculator().add(5, -6)
        self.assertEqual(result, -1)
        
    def test_add_sameNumber_differentsigns(self):
        result = SimpleCalculator().add(-5, 5)
        self.assertEqual(result, 0)
       
    
    #subtract
    def test_subtract_a_greater(self):
        result = SimpleCalculator().subtract(6, 5)
        self.assertEqual(result, 1)
       
    def test_subtract_b_greater(self):
        result = SimpleCalculator().subtract(6, 7)
        self.assertEqual(result, -1)
       
    def test_subtract_b_negative(self):
        result = SimpleCalculator().subtract(6, -5)
        self.assertEqual(result, 11)


    #multiply
    def test_multiply_OneNegative(self):
        result = SimpleCalculator().multiply(6, -5)
        self.assertEqual(result, -30)

    def test_multiply_bothNegative(self):
        result = SimpleCalculator().multiply(-6, -5)
        self.assertEqual(result, 30)

    def test_multiply_positive(self):
        result = SimpleCalculator().multiply(6, 5)
        self.assertEqual(result, 30)
    
    #Divide
    try:
        def test_divide_aGreater(self):
            result = SimpleCalculator().divide(6, 3)
            self.assertEqual(result, 2)

        def test_divide_bGreater(self):
            result = float(SimpleCalculator().divide(3, 6))
            self.assertEqual(result, 0.5)

        def test_divide_(self):
            result = SimpleCalculator().divide(6, 3)
            self.assertEqual(result, 2)

        def test_divide_byZero(self):
            result = SimpleCalculator().divide(6, 0)
            self.assertEqual(result, None)


    finally:
        print('complete')
      
