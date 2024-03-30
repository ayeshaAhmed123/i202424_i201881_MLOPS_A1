import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_valid_input(self):
        data = {
            'Avg. Session Length': 0.7,
            'Time on App': 0.6,
            'Time on Website': 0.5,
            'Length of Membership': 0.8
        }
        response = self.app.post('/predict', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.json)  # Corrected line
        print("Test 'test_valid_input' passed successfully!")

    def test_missing_feature(self):
        data = {
            'Avg. Session Length': 0.7,
            'Time on App': 0.6,
            # Missing 'Time on Website'
            'Length of Membership': 0.8
        }
        response = self.app.post('/predict', json=data)
        self.assertEqual(response.status_code, 400)
        print("Test 'test_missing_feature' passed successfully!")

    def test_non_numeric_feature(self):
        data = {
            'Avg. Session Length': 0.7,
            'Time on App': 0.6,
            'Time on Website': '0.5',  # Non-numeric value
            'Length of Membership': 0.8
        }
        response = self.app.post('/predict', json=data)
        self.assertEqual(response.status_code, 400)
        print("Test 'test_non_numeric_feature' passed successfully!")

if __name__ == '__main__':
    unittest.main()
########