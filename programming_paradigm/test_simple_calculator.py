import unittest
from simple_calculator import SimpleCalculator;

class Test_SimpleCalculator(unittest.TestCase):
 
    def setUp(self):
        self.calc = SimpleCalculator()
 
    #add
    def test_addition(self):
        self.assertEqual(self.calc.add(5, 6), 11)
        self.assertEqual(self.calc.add(5, -6), -1)
        self.assertEqual(self.calc.add(5, -5), 0)

       
    
    #subtract
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 6), -1)
        self.assertEqual(self.calc.subtract(5, -6), 11)
        self.assertEqual(self.calc.subtract(6, -5), 1)
 
 
    #multiply
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 6), 30)
        self.assertEqual(self.calc.multiply(-5, -6), 30)
        self.assertEqual(self.calc.multiply(5, -5), -25)


    #Divide
    try:
        def test_dision(self):
            self.assertEqual(self.calc.divide(6, 3), 2)
            self.assertEqual(self.calc.divide(3, 6), 0.5)
            self.assertEqual(self.calc.divide(5, -5), -1)
            self.assertEqual(self.calc.divide(5, 0), None)
      

    finally:
        print('complete')
      
