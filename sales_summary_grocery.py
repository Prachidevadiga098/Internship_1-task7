
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create SQLite database and insert sample grocery data
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

# Insert NEW grocery sample sales data
sample_data = [
    ('Milk', 20, 45.0),
    ('Bread', 30, 25.0),
    ('Eggs', 50, 6.0),
    ('Butter', 10, 80.0),
    ('Cheese', 5, 120.0),
    ('Milk', 15, 44.0),
    ('Bread', 25, 24.0),
    ('Eggs', 40, 6.5),
    ('Butter', 8, 78.0),
    ('Cheese', 6, 115.0)
]
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# Step 2: Query total quantity and revenue by product
query = '''
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
'''

df = pd.read_sql_query(query, conn)

# Step 3: Print the result
print("Sales Summary:")
print(df)

# Step 4: Plot revenue as a bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False, color='green')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (INR)")
plt.tight_layout()

# Step 5: Save the chart
plt.savefig("sales_chart.png")
plt.show()

# Close connection
conn.close()
