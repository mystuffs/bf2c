from unittest import TestCase

from bf2c.bf2c import BFConverter

BF = ',[[>+>+<<-]>>[<<+>>-]<<-]>.<'


class TestBF2C(TestCase):
    def test_convert_to_c(self):
        BFConverter().convert2file('test', BF)

    def test_convert_to_cpp(self):
        BFConverter(language='cpp').convert2file('test', BF)

    def test_language(self):
        b = BFConverter()
        self.assertEqual(b.language, 'c', 'Default language should be C.')
        b.language = 'cpp'
        self.assertEqual(b.language, 'cpp', 'Should be changed to C++.')
        b.language = 'c'
        self.assertEqual(b.language, 'c', 'Should be changed back to C.')

        def f(*args):
            nonlocal b
            b.language = 'java'

        self.assertRaises(ValueError, f, 'Should raise Value Error.')
