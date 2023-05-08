'''Test module the translator'''

import unittest

import translator

class TestTranslator(unittest.TestCase):
    ''' Translator test class'''

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour', "OK")
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(english_to_french(None), '')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english(None), '')


unittest.main()
