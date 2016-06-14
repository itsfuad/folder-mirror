import unittest
from folder_mirror import analyze

class AnalyzeTest(unittest.TestCase):
    def test_sample(self):
        with open('examples/input.txt', encoding='utf-8') as f:
            result=analyze(f.read())
        self.assertIsInstance(result,dict)
        self.assertTrue(result)

if __name__ == '__main__': unittest.main()

class EmptyInputTest(unittest.TestCase):
    def test_empty_input(self):
        # Empty input is either a valid empty dataset or an explicit error.
        try:
            output=analyze('')
            self.assertIsInstance(output, dict)
        except (ValueError, TypeError):
            pass
