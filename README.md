# Wishlist

## Python version

    >= Python 3.8 32 Bits version

## Python dependencies

    pip install -r requirements.txt

## MongoDB
It's need to change the PRODUCTION_SERVER_IP variable in Databse.database.py to your cluster
    
    EX: PRODUCTION_SERVER_IP: Final[str] = "mongodb://localhost:27017/"
    
the database have the Database "Wishlist" and the Collections "client_list" and "list".
Please create their in your cluster 

## How to start
You will execute the file below:

    main.py
    
and with your browser, you will send the urls below according to your needs:
    
### New Client
< NAME> - Your Name

< EMAIL> - Your e-mail
    
    http://localhost:5000/create_new_client/<NAME>/<EMAIL>

### Delete Client

If you want, you can delete your user

< NAME> - Your Name

< EMAIL> - Your e-mail
    
    http://localhost:5000/delete_client/<NAME>/<EMAIL>
   
   
### Show the products

< PAGE> - represent the page number with the products

    http://localhost:5000/list_page/<PAGE>
    
### New Favorite List
If you want, you can add a favorite list for your item

< NAME> - Your Name

< ITEM> - ID Item
    
    http://localhost:5000/register_new_list/<NAME>/<ITEM>
    
### Add new item in your Favorite List

< NAME> - Your Name

< ITEM> - ID Item
    
    http://localhost:5000/add_new_item/<NAME>/<ITEM>
    
### Delete an item in your Favorite List

< NAME> - Your Name

< ITEM> - ID Item
    
    http://localhost:5000/delete_item_list/<NAME>/<ITEM>
