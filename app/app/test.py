"Sample Test"

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    
    def test_add_args(self):
        # Add arguments
        res = calc.add(2,3,5)
        
        self.assertEqual(res, 10)
        
    def test_subtract_args(self):
        # Subtract arguments
        res = calc.subtract(10,5,3,2)
        
        self.assertEqual(res, 0)