import pathlib
import unittest

from check_links.config import Config


class TestConfig(unittest.TestCase):
    def setUp(self):
        pass

    def test_config(self):
        config = Config("config.yaml")
        self.assertEqual(config.content.path, pathlib.Path("../../content"))


if __name__ == "__main__":
    unittest.main()
