import sqlite3


def get_all_genres():
    conn = sqlite3.connect('chinook.db')
    cursor = conn.cursor()

    query = "SELECT Name FROM genres"
    cursor.execute(query)
    genres = [row[0] for row in cursor.fetchall()]
    conn.close()

    return genres


print(get_all_genres())
