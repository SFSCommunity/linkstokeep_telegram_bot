from datetime import datetime
from pymongo import MongoClient


class Mongo():

    def __init__(self, db="savelink", collection="mycollection"):
        self.__client = MongoClient()
        self.__db = self.__client[db]
        self.__collection = self.__db[collection]

    def Insert(self, title, lang, link):

        data = {
            "title": title,
            "lang": lang,
            "link": link,
            "created_date": datetime.now()
        }

        self.__collection.insert(data)

    def get_all(self):

        return list(self.__collection.find())

    def get_query(self, **kwargs):

        if "title" and "link" and "lang" in kwargs:
            return self.__collection.find({"title": kwargs["title"],
                                           "link": kwargs["link"],
                                           "lang": kwargs["lang"]})


    def delete_query(self, **kwargs):

        if "title" in kwargs:
            self.__collection.delete_many({"title": kwargs["title"]})
        elif "link" in kwargs:
            self.__collection.delete_many({"link": kwargs["link"]})
        else:
            raise BaseException("Add link or title")