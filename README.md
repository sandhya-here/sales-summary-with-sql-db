# 📊 SQLite Sales Summary Project

This is a simple Python project that uses an SQLite database to store and analyze sales data using SQL queries and `pandas`.

## 🔧 Tools & Libraries Used

- SQLite (`sqlite3`)
- Pandas
- Matplotlib
- Python 3.x

## 📁 Files in the Project

- `analyze.py`: Python script that connects to SQLite DB, runs SQL, loads data, and plots a chart.
- `task7.1`: Sample database containing product sales.
- `output.png`: Output bar chart showing revenue by product.
- `README.md`: Project overview (this file!).

## 🧠 SQL Query Used

```sql
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
