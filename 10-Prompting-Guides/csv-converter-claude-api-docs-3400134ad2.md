---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:20Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/csv-converter"
title: "CSV converter - Claude API Docs"
---

# CSV converter


Convert data from various formats (JSON, XML, etc.) into properly formatted CSV files.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example Output

Based on the provided JSON data and requirements, here's the converted CSV file:

csv

``` shiki
"name";"age";"city";"email"
"John Doe";"30";"New York";"john.doe@example.com"
"Jane Smith";"25";"London";"jane.smith@example.com"
"Bob Johnson";"35";"Paris";"bob.johnson@example.com"
```

Explanation:

- The first line of the CSV file contains the column headers: "name", "age", "city", and "email", separated by semicolons (;) and enclosed in double quotes (").
- Each subsequent line represents a row of data, with values separated by semicolons (;) and enclosed in double quotes (").
- The order of the values in each row corresponds to the specified column order: name, age, city, and email.
- Special characters, if present in the values, are preserved within the double quotes.

To save the CSV file:

1.  Copy the CSV data provided above.
2.  Open a text editor (e.g., Notepad, TextEdit, or any other plain text editor).
3.  Paste the CSV data into the text editor.
4.  Save the file with a .csv extension (e.g., data.csv).

Note: When opening the CSV file in a spreadsheet application (e.g., Microsoft Excel, Google Sheets), make sure to specify the correct delimiter (semicolon) and the presence of double quotes around the values to ensure proper formatting.

------------------------------------------------------------------------

## 

API Request

Python

Python

TypeScript

TypeScript

AWS Bedrock Python

AWS Bedrock Python

AWS Bedrock TypeScript

AWS Bedrock TypeScript

Vertex AI Python

Vertex AI Python

Vertex AI TypeScript

Vertex AI TypeScript

``` shiki
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    temperature=0,
    system="As a data conversion expert, your task is to convert data from different formats (JSON, XML, etc.) into properly formatted CSV files. The user will provide the input data in the original format, along with any specific requirements or preferences for the CSV output (e.g., column order, delimiter, encoding). Ensure that you have a clear understanding of the data structure and the desired CSV format, asking any clarifying questions as needed. Once you have the necessary information, generate the CSV output by following the appropriate formatting rules, such as using commas as delimiters, enclosing values in quotes if necessary, and handling special characters or line breaks correctly. Finally, provide any additional instructions or tips for saving or using the CSV file.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": 'Please convert the following JSON data into a CSV file: \n \n[ \n { \n "name": "John Doe", \n "age": 30, \n "city": "New York", \n "email": "[email protected]" \n }, \n { \n "name": "Jane Smith", \n "age": 25, \n "city": "London", \n "email": "[email protected]" \n }, \n { \n "name": "Bob Johnson", \n "age": 35, \n "city": "Paris", \n "email": "[email protected]" \n } \n] \n \nRequirements: \n- Columns in the CSV should be in the order: name, age, city, email \n- Use semicolons (;) as delimiters \n- Enclose all values in double quotes (")',
                }
            ],
        }
    ],
)
print(message.content)
```
