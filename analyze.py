import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('sales_data.db')

# Run SQL query
query = '''
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
'''

# Load into pandas
df = pd.read_sql_query(query, conn)

# Close the DB connection
conn.close()

# Print result
print("\n📊 Sales Summary:\n")
print(df)

# Plot bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title('Revenue by Product')
plt.ylabel('Revenue')
plt.xlabel('Product')
plt.tight_layout()
plt.savefig("sales_chart.png")  # Optional
plt.show()
