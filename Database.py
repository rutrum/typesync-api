import mysql.connector
from mysql.connector import errorcode


pass_file = open("root_pass.txt")
root_pass = pass_file.read().strip()

try:
    cnx = mysql.connector.connect(
        host='35.193.10.101',
        database='lyrictypingtestdb',
        user='root',
        password=root_pass
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()


def add_new_score(name, artist, title, time, score):
    