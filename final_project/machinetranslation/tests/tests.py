import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslateEnToFr(unittest.TestCase):
    """
    Class to test the function englishToFrench
    """
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertNotEqual(englishToFrench('Bye'),'Bonjour')
        #self.assertIsNone(englishToFrench(None))

class TestTranslateFrToEn(unittest.TestCase):
    """
    Class to test the function frenchToEnglish
    """
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'),'Bye')
        #self.assertIsNone(frenchToEnglish(None))

if __name__ == '__main__':
    unittest.main()