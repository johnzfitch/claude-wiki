::: {.cell .markdown}
# How to make SQL queries with Claude

In this notebook, we\'ll explore how to use Claude to generate SQL
queries based on natural language questions. We\'ll set up a test
database, provide the schema to Claude, and demonstrate how it can
understand and translate human language into SQL queries.
:::

::: {.cell .markdown}
## Setup

First, let\'s install the necessary libraries and setup our Anthropic
client with our API key.
:::

::: {.cell .code}
``` python
# Install the necessary libraries
%pip install anthropic
```
:::

::: {.cell .code execution_count="2"}
``` python
# Import the required libraries
import sqlite3

from anthropic import Anthropic

# Set up the Claude API client
client = Anthropic()
MODEL_NAME = "claude-opus-4-1"
```
:::

::: {.cell .markdown}
## Creating a Test Database

We\'ll create a test database using SQLite and populate it with sample
data:
:::

::: {.cell .code execution_count="3"}
``` python
# Connect to the test database (or create it if it doesn't exist)
conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary INTEGER
    )
""")

# Insert sample data
sample_data = [
    (1, "John Doe", "Sales", 50000),
    (2, "Jane Smith", "Engineering", 75000),
    (3, "Mike Johnson", "Sales", 60000),
    (4, "Emily Brown", "Engineering", 80000),
    (5, "David Lee", "Marketing", 55000),
]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", sample_data)
conn.commit()
```
:::

::: {.cell .markdown}
## Generating SQL Queries with Claude

Now, let\'s define a function to send a natural language question to
Claude and get the generated SQL query:
:::

::: {.cell .code execution_count="8"}
``` python
# Define a function to send a query to Claude and get the response
def ask_claude(query, schema):
    prompt = f"""Here is the schema for a database:

{schema}

Given this schema, can you output a SQL query to answer the following question? Only output the SQL query and nothing else.

Question: {query}
"""

    response = client.messages.create(
        model=MODEL_NAME, max_tokens=2048, messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
```
:::

::: {.cell .markdown}
We\'ll retrieve the database schema and format it as a string:
:::

:::: {.cell .code execution_count="5"}
``` python
# Get the database schema
schema = cursor.execute("PRAGMA table_info(employees)").fetchall()
schema_str = (
    "CREATE TABLE EMPLOYEES (\n" + "\n".join([f"{col[1]} {col[2]}" for col in schema]) + "\n)"
)
print(schema_str)
```

::: {.output .stream .stdout}
    CREATE TABLE EMPLOYEES (
    id INTEGER
    name TEXT
    department TEXT
    salary INTEGER
    )
:::
::::

::: {.cell .markdown}
Now, let\'s provide an example natural language question and send it to
Claude:
:::

:::: {.cell .code execution_count="9"}
``` python
# Example natural language question
question = "What are the names and salaries of employees in the Engineering department?"
# Send the question to Claude and get the SQL query
sql_query = ask_claude(question, schema_str)
print(sql_query)
```

::: {.output .stream .stdout}
    SELECT name, salary
    FROM EMPLOYEES
    WHERE department = 'Engineering';
:::
::::

::: {.cell .markdown}
## Executing the Generated SQL Query

Finally, we\'ll execute the generated SQL query on our test database and
print the results:
:::

:::: {.cell .code execution_count="10"}
``` python
# Execute the SQL query and print the results
results = cursor.execute(sql_query).fetchall()

for row in results:
    print(row)
```

::: {.output .stream .stdout}
    ('Jane Smith', 75000)
    ('Emily Brown', 80000)
:::
::::

::: {.cell .markdown}
Don\'t forget to close the database connection when you\'re done:
:::

::: {.cell .code execution_count="11"}
``` python
# Close the database connection
conn.close()
```
:::
