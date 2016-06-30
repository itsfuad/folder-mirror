import json, os, subprocess, sys, unittest

class CliTest(unittest.TestCase):
    def test_json_output(self):
        result=subprocess.check_output([sys.executable,'cli.py','examples/input.txt'])
        self.assertIsInstance(json.loads(result.decode('utf-8')), dict)
    def test_stdin(self):
        process=subprocess.run([sys.executable,'cli.py','-'],input=b'',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.assertIn(process.returncode,(0,2))
