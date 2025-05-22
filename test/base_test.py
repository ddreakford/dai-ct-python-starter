import unittest
import urllib.parse
import os


class BaseTest(unittest.TestCase):

    def setUp(self):
        access_key = os.environ.get('CT_ACCESS_KEY')
        # print(f"Access Key: {access_key}")
        if access_key:
            self.options.set_capability('accessKey', access_key)

    def getUrl(self):
        cloud_url = urllib.parse.urljoin(os.environ.get('CT_URL'), '/wd/hub')
        print(f"CT URL: {cloud_url}")
        return cloud_url

if __name__ == '__main__':
    unittest.main()