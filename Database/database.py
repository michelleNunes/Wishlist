import pymongo.common
from typing import Final
from pymongo import MongoClient, errors
from Service.list_service import ListService

PRODUCTION_SERVER_IP: Final[str] = "mongodb://localhost:27017/"


class DataBase(object):
    try:
        db: MongoClient = MongoClient(
            PRODUCTION_SERVER_IP,
            retryWrites=False,
            serverSelectionTimeoutMS=10000,
        )["Wishlist"]
    except pymongo.errors.ServerSelectionTimeoutError:
        print(f"Using MongoDB from localhost")
        db: MongoClient = MongoClient(
            PRODUCTION_SERVER_IP, retryWrites=False
        )
        database = db["Wishllist"]
        collection1 = database["client_list"]
        collection2 = database["list"]

    class ClientRegistered(Exception):
        pass

    class ClientNotRegistered(Exception):
        pass

    class ListNotExist(Exception):
        pass

    class ListAlreadyExist(Exception):
        pass

    @staticmethod
    def create_new_client(name, email):
        find_client = DataBase.db.client_list.find_one({"name": name, "email": email})
        if find_client is not None:
            raise DataBase.ClientRegistered("Client already registered, try to register another e-mail")
        else:
            dict_values = {
                "name": name,
                "email": email
            }
            DataBase.db.client_list.insert_one(dict_values)

    @staticmethod
    def delete_client(name, email):
        find_client = DataBase.db.client_list.find_one({"name": name, "email": email})

        if find_client is None:
            raise DataBase.ClientNotRegistered("Client Not Registered")
        else:
            DataBase.db.list.delete_one({"name": name})
            DataBase.db.client_list.delete_one({"name": name, "email": email})

    @staticmethod
    def delete_item_list(name, item):
        find_list = DataBase.db.list.find_one({"name": name, "list": item})

        if find_list is None:
            raise DataBase.ListNotExist("Item doesn't exist in your list, please check the ID")
        else:
            DataBase.db.list.delete_one({"name": name, "list": item})

    @staticmethod
    def create_new_list(name, list):
        find_list = DataBase.db.list.find_one({"name": name})

        if find_list is not None:
            raise DataBase.ListAlreadyExist("Favorite List already exist")
        else:
            DataBase.db.list.insert_one(
                {"name": name, "list": list})

    @staticmethod
    def update_list(name, new_fav):
        find_list = DataBase.db.list.find({"name": name})

        if find_list is None:
            raise DataBase.ListNotExist("Favorite List doesn't exist")
        else:
            if (DataBase.db.list.find({"name": name, "list": new_fav})) is None:
                DataBase.db.list.insert(
                    {"name": name, "list": new_fav})
                return {
                    "success": True,
                    "message": f" New item insert in the list",
                }
            else:
                raise DataBase.ListAlreadyExist("Favorite item already exist in your list")

    @staticmethod
    def show_fav_list(name):
        response = []
        query_filter = {"name": name}
        find_list = DataBase.db.list.find(query_filter).sort(
            [("list", pymongo.ASCENDING)]
        )
        if find_list is None:
            raise DataBase.ListNotExist("Favorite List doesn't exist")
        else:
            for list in find_list:
                result = ListService.find_list_id(list['list'])
                response.append(result)

            return response
