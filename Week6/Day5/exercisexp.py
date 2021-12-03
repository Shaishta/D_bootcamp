#Exercise 1 : Restaurant Menu Manager
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '5427'
DATABASE = 'menu_manager'

conn_string = "host='localhost' dbname='menu_manager' user='postgres' password='5427'"
connection = psycopg2.connect(conn_string)
cursor = connection.cursor()


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        save_items = f"insert into menu (item_name, price) values ('{self.name}', {self.price});"
        cursor.execute(save_items)
        connection.commit()
        print('item successfully added.')

    def delete(self):
        del_items = f"delete from menu where item_name = '{self.name}';"
        cursor.execute(del_items)
        connection.commit()

    def update(self, name, price):
        update_items = f"update menu set item_name ='{name}', price = {price} where item_name = '{self.name}'"
        cursor.execute(update_items)
        connection.commit()

    @staticmethod
    def all():
        query = "select * from menu;"
        cursor.execute(query)
        results = cursor.fetchall()
        for item in results:
            print(item)

    @staticmethod
    def get_by_name(name):
        get_item_q = f"select item_name from menu where item_name = '{name}';"
        cursor.execute(get_item_q)
        result = cursor.fetchall()
        if result:
            for item in result:
                return item
        else:
            return None
