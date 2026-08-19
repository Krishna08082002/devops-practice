import unittest
from http.client import HTTPConnection
from threading import Thread
from app.application import server


class TestApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_thread = Thread(
            target=server.serve_forever,
            daemon=True
        )
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        server.shutdown()
        server.server_close()

    def test_home(self):
        connection = HTTPConnection("localhost", 8000)
        connection.request("GET", "/")

        response = connection.getresponse()
        body = response.read().decode()

        self.assertEqual(response.status, 200)
        self.assertEqual(body, "DevOps application v2 is running!")

        connection.close()

    def test_health(self):
        connection = HTTPConnection("localhost", 8000)
        connection.request("GET", "/health")

        response = connection.getresponse()
        body = response.read().decode()

        self.assertEqual(response.status, 200)
        self.assertEqual(body, "OK")

        connection.close()

    def test_not_found(self):
        connection = HTTPConnection("localhost", 8000)
        connection.request("GET", "/anything")

        response = connection.getresponse()

        self.assertEqual(response.status, 404)

        connection.close()


if __name__ == "__main__":
    unittest.main()
