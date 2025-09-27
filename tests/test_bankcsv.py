import unittest
import tempfile
import os
from mybank import bank
# copied from https://sqlpey.com/python/top-4-methods-to-unit-test-file-writing-functions-in-python-using-unittest/
class LambTests(unittest.TestCase):
     def setUp(self):
             self.tempfile= tempfile.NamedTemporaryFile(delete=False, mode='w')
             self.temp_file.write(
                "customer_id,first_name,last_name,password,balance_checking,balance_savings\n"
                "10001,suresh,sigera,juagw362,1000.0,10000.0\n"
            )
     def test_bank_output_with_tempfile(self):
            bank.write_bank(self.tempfile_path)
            temp_file_path = tempfile.name
            with open(temp_file_path, 'r') as f:  
                 content=f.read() 
            self.assertIn("10001",content)
     def tearDown(self):
      os.remove(self.temp_file_path)
if __name__ == "__main__":
    unittest.main()
