import numberutilp2
import unittest

class processor(unittest.TestCase):
    #def t_total(self):
    def test_total(self):
        list=[1,5,7,9]
        osr=numberutilp2.total(list)
        gsr=22
        self.assertEqual(osr,gsr)

    def test_max(self):
        list=[1,5,7,9]
        osr=numberutilp2.max(list)
        gsr=9
        self.assertEqual(osr,gsr)

    def test_min(self):
        list=[1,6,3,46,-1467]
        osr=numberutilp2.min(list)
        gsr=-1467
        'error in numberutilp2.min'
        self.assertEqual(osr,gsr)  

    def test_sq(self):
        b=2
        s=8
        osr=numberutilp2.sq(b,s)
        gsr=256
        self.assertEqual(osr,gsr)          



if __name__=="__main__":
    #unittest.main
    unittest.main()