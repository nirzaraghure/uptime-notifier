import unittest
from unittest import mock
import uptime

class TestWebsiteChecker(unittest.TestCase):
    
    @mock.patch('uptime.requests.get')
    def test_check_website(self, mocked_get):
        # Mocking the response of requests.get()
        mocked_response = mock.Mock()
        mocked_get.return_value = mocked_response
        
        # Case where website is up
        mocked_response.status_code = 200
        mocked_response.raise_for_status.side_effect = None  # simulate successful request without exception
        uptime.check_website()
        
        # Case where website is down due to timeout
        mocked_get.side_effect = Exception('ConnectionTimeout')
        with self.assertRaises(Exception):
            uptime.check_website()
            
        # Case where website returns status other than 200
        mocked_response.status_code = 404
        mocked_response.raise_for_status.side_effect = Exception('RequestException')  # simulate request exception
        uptime.check_website()
        
if __name__ == '__main__':
    unittest<｜begin▁of▁sentence｜>s