class Person:

    def __init__(self, id: int, name: str, age: int):
        self.id: int = id
        self.name: str = name
        self.age: int = age

    def push(self):

        import mysql.connector as connector

        config = {
            'user': 'somesh',
            'password': 'someshPass',
            'host': 'db',
            'port': '3306',
            'database': 'someshDB'
        }
        try:
            connection = connector.connect(**config)
            insert_query = """INSERT INTO information(id, name, age) values ({}, "{}", {});""".format(self.id,
                                                                                                      self.name,
                                                                                                      self.age)
            cursor = connection.cursor()
            result = cursor.execute(insert_query)
            connection.commit()
        except Exception as e:
            print("failed with exception" + e)
        finally:
            connection.close()

    def getList():

        import mysql.connector as connector

        config = {
            'user': 'somesh',
            'password': 'someshPass',
            'host': 'db',
            'port': '3306',
            'database': 'someshDB'
        }
        connection = connector.connect(**config)

        select_all_query = """SELECT * FROM information"""
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS information(id integer primary key, name varchar(25), age integer);")
        cursor.execute(select_all_query)
        data = cursor.fetchall()
        connection.close()
        return data

    def delete(id: int):
        import mysql.connector as connector

        config = {
            'user': 'somesh',
            'password': 'someshPass',
            'host': 'db',
            'port': '3306',
            'database': 'someshDB'
        }
        try:
            connection = connector.connect(**config)
            delete_query = """delete from information where id={};""".format(id)
            cursor = connection.cursor()
            result = cursor.execute(delete_query)
            connection.commit()
        except Exception as e:
            print("failed with exception" + e)
        finally:
            connection.close()

    def search(id: int):
        import mysql.connector as connector

        config = {
            'user': 'somesh',
            'password': 'someshPass',
            'host': 'db',
            'port': '3306',
            'database': 'someshDB'
        }
        try:
            connection = connector.connect(**config)
            search_query = """select * from information where id={};""".format(id)
            cursor = connection.cursor()
            cursor.execute(search_query)
            result = cursor.fetchall()
            connection.commit()
        except Exception as e:
            print("failed with exception" + e)
        finally:
            connection.close()
            return result

    def update(self):
        import mysql.connector as connector

        config = {
            'user': 'somesh',
            'password': 'someshPass',
            'host': 'db',
            'port': '3306',
            'database': 'someshDB'
        }
        try:
            connection = connector.connect(**config)
            update_query = """UPDATE information SET name='{}', age={} WHERE id={};""".format(self.name, self.age,
                                                                                              self.id)
            cursor = connection.cursor()
            result = cursor.execute(update_query)
            connection.commit()
        except Exception as e:
            print("failed with exception" + e)
        finally:
            connection.close()
