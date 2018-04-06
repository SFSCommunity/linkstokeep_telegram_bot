from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
from database import Mongo
from own_filter import LinkFilter




class TelegramBot():

    def __init__(self, token, channel_name="denemeeedeee"):
        self.__updater = Updater(token=token)
        self.__dispatcher = self.__updater.dispatcher
        self.__mongo = Mongo()
        self.channel_name = channel_name

    def get_link(self, bot, update):

        if not self.channel_name == update.channel_post.chat.username:
            return False

        msg = str(update.channel_post.text)
        split_msg = msg.split("-", 2)
        title = split_msg[0]
        lang = split_msg[1].replace("[", "").replace("]", "")
        link = split_msg[2]
        self.__mongo.Insert(title, lang, link)
        return True

    def set_handler(self):
        f = LinkFilter()
        self.__get_link_handler = MessageHandler(f, self.get_link, channel_post_updates=True)

    def set_dispatcher(self):
        self.__dispatcher.add_handler(self.__get_link_handler)

    def start(self):
        self.__updater.start_polling()


bot = TelegramBot(token=Token)
bot.set_handler()
bot.set_dispatcher()
bot.start()
