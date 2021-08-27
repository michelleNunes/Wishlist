from flask import Flask
from Database.database import DataBase
from Service.list_service import ListService

app = Flask(__name__)


@app.route("/create_new_client/<name>/<email>")
def create_new_client(name, email):
    try:
        DataBase.create_new_client(name, email)
        return {
            "success": True,
            "message": f" Client {name} - {email} registered",
        }
    except(
            Exception
    ) as exception:
        return {"error": str(exception)}


@app.route("/delete_client/<name>/<email>")
def delete_client(name, email):
    try:
        DataBase.delete_client(name, email)
        return {
            "success": True,
            "message": f"Client {name} - {email} Delete",
        }
    except(DataBase.ClientNotRegistered) as exception:
        return {"error": str(exception)}

@app.route("/list_page/<page>")
def list_page(page):
    try:
        result = ListService.find_list_page(page)
        return result
    except Exception as exception:
        return {"error": "Cannot connect to the server," + str(exception)}

@app.route("/register_new_list/<name>/<item>")
def register_new_list(name, item):
    try:
        DataBase.create_new_list(name, item)
        return {
            "success": True,
            "message": f" New List registered",
        }
    except(
            Exception
    ) as exception:
        return {"error": str(exception)}

@app.route("/add_new_item/<name>/<item>")
def add_new_item(name, item):
    try:
        DataBase.update_list(name, item)
        return {
            "success": True,
            "message": f" New item registered",
        }
    except(
            Exception
    ) as exception:
        return {"error": str(exception)}

@app.route("/show_favorite_list/<name>")
def show_favorite_list(name):
    try:
        result = DataBase.show_fav_list(name)
        return {
            "Name": name,
            "Favorite List": result,
        }
    except(
            Exception
    ) as exception:
        return {"error": str(exception)}

@app.route("/delete_item_list/<name>/<item>")
def delete_item_list(name, item):
    try:
        DataBase.delete_item_list(name, item)
        return {
            "success": True,
            "message": f" item deleted",
        }
    except(
            Exception
    ) as exception:
        return {"error": str(exception)}

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
