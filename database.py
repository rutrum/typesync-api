import mysql.connector
from mysql.connector import errorcode
from mysql.connector.cursor import MySQLCursor


pass_file = open("root_pass.txt")
root_pass = pass_file.read().strip()


def connect_to_db():
    return mysql.connector.connect(
            host='35.193.10.101',
            database='typingtest',
            user='root',
            password=root_pass
    )


def add_new_score(name, geniusID, time, score, spotifyID):
    cnx = connect_to_db()
    insert = cnx.cursor()
    query = "INSERT INTO entries (username, geniusID, milliseconds, time, spotifyID) VALUES (%s, %s, %s, %s, %s);"
    val = (name, int(geniusID), int(time), int(score), spotifyID)
    insert.execute(query, val)
    cnx.commit()

    print("Record (", name, "\b,", score, "\b,", geniusID, ") inserted")
    cnx.close()


def get_song_leaderBoard(geniusID, listLength):
    cnx = connect_to_db()
    get = cnx.cursor(dictionary=True)
    query = "SELECT * FROM entries WHERE geniusID = %s ORDER BY time ASC LIMIT %s;"
    val = (int(geniusID), int(listLength))
    get.execute(query, val)
    results = get.fetchall()
    cnx.close()

    print("Fetched", listLength, "records for song", geniusID)
    return {'results': results}


def alter_table():
    alter = cnx.cursor()
    query = "ALTER TABLE entries CHANGE songID geniusID INT;"
    alter.execute(query)
    cnx.commit()
    cnx.close()

def get_all():
    get = cnx.cursor()
    query = "SELECT * FROM entries;"
    get.execute(query)



def main():
    #add_new_score('HandRob', '86916', '92393', '9344', '08dFHFTx6r67MTsYn5ilDR')
    #get_all()
    #alter_table()
    cnx.close()


if __name__ == "__main__":
    main()
