import sys 
sys.path.append("delivery_network/")

import unittest
from question18 import trucks_filtre

class Test_trucks_filtre(unittest.TestCase):
    def test_trucks1(self):
        T=trucks_filtre("input/trucks.1.in")
        self.assertEqual(len(T),2)
        self.assertEqual((2000000,200000) in T,True)

    def test_trucks2(self):
        T=trucks_filtre("input/trucks.2.in")
        self.assertEqual((2500000,370000) in T,False)
        self.assertEqual((3000000,360000) in T,True)

    def test_trucks3(self):
        T=trucks_filtre("input/trucks.3.in")
        self.assertEqual((3000,365) in T,False)
        self.assertEqual((4000,220) in T,True)

if __name__ == '__main__':
    unittest.main()