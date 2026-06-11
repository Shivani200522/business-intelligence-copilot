from backend.services.sql_generator_service import generate_sql

schema = """
Table: sales_dataset

Columns:
date
product
quantity
price
region
"""

question = """
Which region generated highest revenue?
"""

sql = generate_sql(
    schema=schema,
    question=question
)

print(sql)