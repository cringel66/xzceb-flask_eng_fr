""" This test translator pyton """
import unittest
from translator import englishToFrench,frenchToEnglish

class TestTranslator(unittest.TestCase):
    """ Test english and french translation """
    def test_NullFrenchToEnglish(self):
        """ Test for null input for frenchToEnglish """
        self.assertNotEqual(frenchToEnglish(None), '')

    def test_NullEnglishToFrench(self):
        """ Test for null input for englishToFrench. """
        self.assertNotEqual(englishToFrench(None), '')

    def test_TransEnglishToFrench(self):
        """ Test for the translation of the world ‘Hello’ and ‘Bonjour’ """
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_TransFrenchToEnglish(self):
        """ Test for the translation of the world ‘Bonjour’ and ‘Hello’ """
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

unittest.main()
