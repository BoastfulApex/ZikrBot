import sqlite3
from sqlite3 import Error


def post_sql_query(sql_query):
    with sqlite3.connect('my.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
        except Error:
            pass
        result = cursor.fetchall()
        return result


def create_tables():
    users_query = '''CREATE TABLE IF NOT EXISTS USERS
                        (user_id INTEGER PRIMARY KEY NOT NULL,
                        ismi TEXT);'''

    post_sql_query(users_query)


def add_table_requests():
    users_query = '''CREATE TABLE IF NOT EXISTS REQUESTS
                        (req_id INTEGER NOT NULL,
                        user_id INTEGER NOT NULL,
                        ship_id TEXT,
                        cost INTEGER);'''

    post_sql_query(users_query)

def register_user(user, ism):
    user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO USERS (user_id, ismi) VALUES ({user}, "{ism}");'
        post_sql_query(insert_to_db_query)
    else:
        insert_to_db_query = f'UPDATE USERS set ismi = "{ism}" WHERE user_id={user};'
        post_sql_query(insert_to_db_query)


create_tables()


def gg(user_id):
    con = sqlite3.connect('my.db')
    cur = con.cursor()
    cur.execute(f'SELECT lang FROM USERS where user_id={int(user_id)}')
    us = cur.fetchone()
    return us


def users_id():
    con = sqlite3.connect('my.db')
    cur = con.cursor()
    cur.execute(f'SELECT user_id FROM USERS')
    us = cur.fetchall()
    return us


def all_users():
    con = sqlite3.connect('my.db')
    cur = con.cursor()
    cur.execute(f'SELECT * FROM USERS')
    us = cur.fetchall()
    return us