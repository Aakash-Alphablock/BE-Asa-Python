
from django.test import TestCase
from bot import dal

class BotDalTests(TestCase):
    def test_create_new_bot(self):
        bot = dal.create_new_bot(name='Test Bot', description='Test Bot Description', token='test_token', user_id=1, is_demo_bot=True)
        self.assertEqual(bot.name, 'Test Bot')
        self.assertEqual(bot.description, 'Test Bot Description')
        self.assertEqual(bot.token, 'test_token')
        self.assertEqual(bot.user_id, 1)
        self.assertEqual(bot.is_demo_bot, True)

    def test_get_bot_details(self):
        bot = dal.create_new_bot(name='Test Bot', description='Test Bot Description', token='test_token', user_id=1, is_demo_bot=True)
        bot_id = bot.id
        with self.subTest('When bot id is found'):
            bot = dal.get_bot_details(bot_id)
            self.assertEqual(bot.name, 'Test Bot')
            self.assertEqual(bot.description, 'Test Bot Description')
            self.assertEqual(bot.token, 'test_token')
            self.assertEqual(bot.user_id, 1)
            self.assertEqual(bot.is_demo_bot, True)

        with self.subTest('When bot id is not found'):
            bot = dal.get_bot_details(100)
            self.assertEqual(bot, None)