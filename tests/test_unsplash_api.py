import unittest 
import requests
from unittest import TestCase
from unittest.mock import patch
from apis import unsplash_api
from unsplash_mock_data import response, trip_w_pic, trip_no_pic



class TestUnsplashApi(TestCase):
    @patch('unsplash_api._unsplash_api_call')
    def test_api_query(self, mock_response):
        m_response = response #create fake response with fake image urls
        mock_response.side_effect = m_response
        mock_trip_no_pics = trip_no_pic #create trip object with no pics
        trip_object_with_pics = unsplash_api.get_park_image(mock_trip_no_pics) #call method to add pics to trip object
        expected_trip_object_with_pics = trip_w_pic #create second trip object that has right pictures
        #compare return from that method - should have the proper
        self.assertEqual(expected_trip_object_with_pics, trip_object_with_pics)

if __name__ == '__main__':
    unittest.main()