import re
from telegram.ext import BaseFilter


class LinkFilter(BaseFilter):

    name = "Filters.link"

    def filter(self, message):
        return bool(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message.text))

