import sys
sys.path.append("../")

import unittest

import Algmarket
from Algmarket.datadirectory import DataDirectory
from Algmarket.data import DataObjectType
from Algmarket.acl import Acl, AclType

class DataDirectoryTest(unittest.TestCase):
    def setUp(self):
        self.client = Algmarket.client()

    def test_get_name(self):
        dir = DataDirectory(self.client, 'data://.my/test_dir')
        if (dir.exists()):
            dir.delete(True)
        dir.create()
        f = dir.file("a.txt")
        f.put("这个是测试文件")

if __name__ == '__main__':
    unittest.main()
