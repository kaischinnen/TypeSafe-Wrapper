import unittest
from unittest.mock import Mock

import httpx2

from main import JevLib


def make_http_client():
    client = Mock(spec=httpx2.Client)
    client.timeout = 10.0 
    return client


class TestJevLibContextManager(unittest.TestCase):
    def test_closes_client_after_context(self):
        http_client = make_http_client()

        with JevLib(api_key="test-key", http_client=http_client) as jevlib:
            self.assertIsInstance(jevlib, JevLib)
            http_client.close.assert_not_called()

        http_client.close.assert_called_once_with()

    def test_closes_client_after_exception(self):
        http_client = make_http_client()

        with self.assertRaisesRegex(RuntimeError, "failed!"):
            with JevLib(api_key="test-key", http_client=http_client):
                raise RuntimeError("failed!")

        http_client.close.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()