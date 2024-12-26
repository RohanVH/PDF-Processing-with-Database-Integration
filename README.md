# PDF Processing with Database Integration

## Overview
This project processes PDF files stored in a database, extracts their contents, and allows for efficient searching of the text using vectorization techniques. It utilizes Python libraries such as `PyPDF2`, `sklearn`, and `oracledb` to connect to an Oracle database and handle PDF files.

## Features
- Connects to an Oracle database to retrieve PDF file paths.
- Extracts text from multiple PDF files.
- Vectorizes the extracted text for efficient searching.
- Implements a search function to find relevant text based on user queries.

## Requirements
- Python 3.x
- Required Python packages:
  - `PyPDF2`
  - `sklearn`
  - `oracledb`
  
You can install the required packages using pip:

```bash
pip install PyPDF2 scikit-learn oracledb
```


## Database Setup
Ensure that you have access to an Oracle database and that the following parameters are configured correctly in the code:

username: Your database username.
password: Your database password.
dsn: The Data Source Name for the database connection.
You also need a table in your database that contains the paths to the PDF files. The SQL query used in the code is:

```sql
SELECT file_path FROM your_pdf_table
``` 
Replace your_pdf_table with the actual name of your table.

## Usage
- Update the database connection parameters in the code.
- Run the Python script to connect to the database and process the PDF files.
- Use the search function to query the text extracted from the PDFs.

### Example:
To search for a specific term in the PDF contents, modify the query_result line in the code:

```python
query_result = search("your search term")
```

## Acknowledgments
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF handling.
- [scikit-learn](https://scikit-learn.org/) for vectorization.
- [oracledb](https://pypi.org/project/oracledb/) for database management.