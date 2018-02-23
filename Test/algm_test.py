import sys
sys.path.append("../")
import os
import unittest

import Algmarket

class AlgmTest(unittest.TestCase):
    def setUp(self):
        self.client = Algmarket.client()

    def test_call_algm(self):
        result = self.client.algm('algm://qihe/MyTensorflow/0.0.2').call(bytearray('我是测试人员','utf-8'))
        print(result.result)

if __name__ == '__main__':
    unittest.main()
