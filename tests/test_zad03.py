import unittest
from unittest.mock import *

from src.zad03.main import Messenger


class MessengerTest(unittest.TestCase):
    def setUp(self):
        self.messenger = Messenger()

    def test_send_message(self):
        self.messenger.template_engine = MagicMock()
        self.messenger.template_engine.create.side_effect = lambda message: message
        self.messenger.mail_server = MagicMock()
        self.messenger.mail_server.send_message.return_value.status_code = 200
        self.assertEqual(200, self.messenger.send_message("Andrzej", "Hello Andrzej!").status_code)

    def test_send_message_service_unavailable(self):
        self.messenger.template_engine = MagicMock()
        self.messenger.template_engine.create.side_effect = lambda message: message
        self.messenger.mail_server = MagicMock()
        self.messenger.mail_server.send_message.return_value.status_code = 503
        self.assertEqual(503, self.messenger.send_message("Andrzej", "Hello Andrzej!").status_code)

    def test_receive_message(self):
        self.messenger.mail_server = MagicMock()
        self.messenger.mail_server.receive_message.return_value = "Hello!"
        self.assertEqual("Hello!", self.messenger.receive_message())

    def test_receive_message_service_unavailable(self):
        self.messenger.mail_server = MagicMock()
        self.messenger.mail_server.receive_message.return_value.status_code = 503
        self.assertEqual(503, self.messenger.receive_message().status_code)

    def tearDown(self):
        self.messenger = None
