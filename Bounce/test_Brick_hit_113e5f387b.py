import unittest
from game import brick_hit

# Each test function should start with 'test_'.
# The name of the class should start with a capital letter, according to standard conventions.

class TestBrickHit(unittest.TestCase):
    
    def setUp(self):
        self.brickHitObj = brick_hit()

    def test_brick_hit(self):
        # Test Scenario: Functionality Check
        self.assertTrue(self.brickHitObj.hit_brick([50, 50, 60, 60])) # We call functions of an object using the 'object.function()' syntax
        self.assertEqual(self.brickHitObj.hit, 1) # We get attributes of an object using the 'object.attribute' syntax
        self.assertEqual(self.brickHitObj.score, "Score: 1")

        # Test Scenario: Brick Missed
        self.assertFalse(self.brickHitObj.hit_brick([5000, 5000, 6000, 6000]))
        self.assertEqual(self.brickHitObj.hit, 1) 

        # Test Scenario: Testing for Multiple Hits
        self.assertTrue(self.brickHitObj.hit_brick([50, 50, 60, 60]))
        self.assertTrue(self.brickHitObj.hit_brick([70, 70, 80, 80]))
        self.assertTrue(self.brickHitObj.hit_brick([90, 90, 100, 100]))
        self.assertEqual(self.brickHitObj.hit, 4)

        # Test Scenario: Testing with Empty Canvas
        # Let's assume brick() creates a rectangular brick based on the four parameters. 
        self.brickHitObj.bricks = [] 
        self.assertFalse(self.brickHitObj.hit_brick([50, 50, 60, 60]))
        
        # Test Scenario: Testing for Entire Brick Line Hits
        self.brickHitObj.bricks = [[50, 50, 60, 60], [70, 70, 80, 80], [90, 90, 100, 100]]
        for brick in self.brickHitObj.bricks:
            self.assertTrue(self.brickHitObj.hit_brick(brick))

        # Test Scenario: Testing with Non-Rectangular Bricks
        self.brickHitObj.bricks = [[50, 50, 60], [70, 70], [90]] 
        self.assertFalse(self.brickHitObj.hit_brick([50, 50, 60, 60]))

        # Test Scenario: Testing for Hit Sound & Input Parameter Edge Cases
        self.assertTrue(self.brickHitObj.hit_brick([2**31-1, 2**31-1, 2**31-1, 2**31-1]))
        self.assertFalse(self.brickHitObj.hit_brick([-2**31, -2**31, -2**31,  -2**31]))

        # Test Scenario: Testing Behaviour with Division by Zero Error 
        self.assertRaises(TypeError, self.brickHitObj.hit_brick([]))

        # Test Scenario: Validate Function Performance
        for i in range(10000000): 
            self.assertTrue(self.brickHitObj.hit_brick([50, 50, 60, 60]))
            self.assertTrue(self.brickHitObj.hit_brick([70, 70, 80, 80]))
            self.assertTrue(self.brickHitObj.hit_brick([90, 90, 100, 100]))

if __name__ == '__main__':
    unittest.main()
