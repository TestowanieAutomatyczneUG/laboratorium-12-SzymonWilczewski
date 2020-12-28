import unittest
from unittest.mock import *

from src.zad02.main import Subscriber


class SubscriberTest(unittest.TestCase):
    def setUp(self):
        self.subscriber = Subscriber()

    def test_add_client(self):
        self.subscriber.add_client = MagicMock(return_value=["Andrzej"])
        self.assertEqual(["Andrzej"], self.subscriber.add_client("Andrzej"))

    def test_remove_client(self):
        self.subscriber.remove_client = MagicMock(return_value=[])
        self.assertEqual([], self.subscriber.remove_client("Andrzej"))

    def test_send_message_to_client(self):
        self.subscriber.clients = ["Andrzej"]
        self.subscriber.send_message = MagicMock(side_effect=lambda client, message: message)
        self.assertEqual("Hello Andrzej!", self.subscriber.send_message_to_client("Andrzej", "Hello Andrzej!"))

    def test_add_client_type_error(self):
        self.subscriber.add_client = MagicMock(side_effect=TypeError("Client is not a string!"))
        with self.assertRaisesRegex(TypeError, "Client is not a string!"):
            self.subscriber.add_client(1)

    def test_add_client_value_error(self):
        self.subscriber.add_client = MagicMock(side_effect=ValueError("Client already exists!"))
        with self.assertRaisesRegex(ValueError, "Client already exists!"):
            self.subscriber.add_client("Andrzej")

    def test_remove_client_type_error(self):
        self.subscriber.remove_client = MagicMock(side_effect=TypeError("Client is not a string!"))
        with self.assertRaisesRegex(TypeError, "Client is not a string!"):
            self.subscriber.remove_client(1)

    def test_send_message_to_client_type_error(self):
        self.subscriber.send_message_to_client = MagicMock(side_effect=TypeError("Client or message is not a string!"))
        with self.assertRaisesRegex(TypeError, "Client or message is not a string!"):
            self.subscriber.send_message_to_client("Andrzej", [])

    def test_send_message_to_client_value_error(self):
        self.subscriber.send_message_to_client = MagicMock(side_effect=ValueError("Client doesn't exist!"))
        with self.assertRaisesRegex(ValueError, "Client doesn't exist!"):
            self.subscriber.send_message_to_client("Andrzej", "Hello Andrzej!")

    def tearDown(self):
        self.subscriber = None
