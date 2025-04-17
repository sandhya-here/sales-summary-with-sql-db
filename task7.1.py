import sqlite3

# Create and connect to database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create the sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Insert sample data
cursor.executemany('''
    INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)
''', [
    ('Pen', 10, 5.0),
    ('Notebook', 5, 15.0),
    ('Pen', 20, 5.0),
    ('Pencil', 30, 2.0),
    ('Notebook', 10, 15.0)
])

# Save and close
conn.commit()
conn.close()

print("✅ Database and table created with sample data!")
