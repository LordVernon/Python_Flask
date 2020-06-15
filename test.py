import unittest
from server import init_app
from config import Config


app = init_app(Config)
app.testing = True


class MyTestCase(unittest.TestCase):
    def test(self):
        with app.test_client() as client:
            result = client.get('/users/users')
            self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
