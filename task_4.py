def bot_init(self, name):
    self.name = name

def bot_send_message(self, message):
    print(message)

def bot_say_name(self):
    print(self.name)

Bot = type('Bot', (), {
    '__init__': bot_init,
    'send_message': bot_send_message,
    'say_name': bot_say_name
})

def telegram_init(self, name):
    super(TelegramBot, self).__init__(name)
    self.url = None
    self.chat_id = None

def telegram_send_message(self, message):
    if self.url is not None and self.chat_id is not None:
        print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")

TelegramBot = type('TelegramBot', (Bot,), {
    '__init__': telegram_init,
    'send_message': telegram_send_message,
    'set_url': lambda self, url: setattr(self, 'url', url),
    'set_chat_id': lambda self, chat_id: setattr(self, 'chat_id', chat_id)
})

some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message("Hello")

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
telegram_bot.send_message('Hello')
telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')
