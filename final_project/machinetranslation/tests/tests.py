import unittest
from machinetranslation import translator


class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')

unittest.main()