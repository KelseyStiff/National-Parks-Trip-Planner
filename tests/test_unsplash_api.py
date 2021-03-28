import unittest 
import requests
from unittest import TestCase
from unittest.mock import patch
from apis import unsplash_api

class TestUnsplashApi(TestCase):
    @patch('unsplash_api._unsplash_api_call')
    def test_api_query(self, mock_query):
        mock_response = "results": [] "urls": {"small": "test"}
       #create fake response with fake image urls
        mock_trip_object_no_pics = {}  #create trip object with no pics
        trip_object_with_pics = unsplash_api.get_park_image(mock_trip_object_no_pics) #call method to add pics to trip object
        expected_trip_object_with_pics = {}  #create second trip object that has right pictures
        #compare return from that method - should have the proper
        self.assertEqual(expected_trip_object_with_pics, trip_object_with_pics)

if __name__ == '__main__':
    unittest.main()