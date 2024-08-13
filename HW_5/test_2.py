from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/stats_by_city')
def stats_by_city():
    genre = request.args.get('genre')

    conn = sqlite3.connect('chinook.db')
    cursor = conn.cursor()

    # Перевірка на жанр
    cursor.execute("SELECT 1 FROM genres WHERE Name = ? LIMIT 1", (genre,))
    if not cursor.fetchone():
        conn.close()
        return "Specified genre does not exist", 404

    # SQL-запит
    query = """
    SELECT c.City
    FROM customers c
    JOIN invoices i ON c.CustomerId = i.CustomerId
    JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
    JOIN tracks t ON ii.TrackId = t.TrackId
    JOIN genres g ON t.GenreId = g.GenreId
    WHERE g.Name = ?
    GROUP BY c.City
    ORDER BY SUM(ii.Quantity) DESC
    LIMIT 1
    """
    cursor.execute(query, (genre,))
    result = cursor.fetchone()
    conn.close()

    return result[0] if result else ""


if __name__ == '__main__':
    app.run(debug=True, port=5000)
