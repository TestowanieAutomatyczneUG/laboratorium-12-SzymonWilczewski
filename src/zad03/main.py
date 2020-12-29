from src.zad03.TemplateEngine import TemplateEngine
from src.zad03.MailServer import MailServer


class Messenger:
    def __init__(self):
        self.template_engine = TemplateEngine()
        self.mail_server = MailServer()

    def send_message(self, to, message):
        return self.mail_server.send_message(to, self.template_engine.create(message))

    def receive_message(self):
        return self.mail_server.receive_message()
