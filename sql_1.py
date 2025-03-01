import sqlite3


conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

query = """
    SELECT genres.Name, SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS Total_Spent
    FROM invoice_items 
    JOIN tracks ON invoice_items.TrackId = tracks.TrackId
    JOIN genres ON tracks.GenreId = genres.GenreId
    JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
    WHERE invoices.InvoiceDate >= '2010-01-01' AND invoices.InvoiceDate < '2011-01-01'
    GROUP BY genres.Name
    ORDER BY Total_Spent DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("Genre | Total Spent")
for genre, total in results:
    print(f"{genre} | ${total:.2f}")

conn.close()