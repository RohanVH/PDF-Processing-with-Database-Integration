import os
import oracledb
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer

# Database connection parameters
username = "your_username"
password = "your_password"
dsn = oracledb.makedsn('192.168.2.80', '1521', service_name='FREEPDB1')

# Connect to the database
try:
    conn = oracledb.connect(user=username, password=password, dsn=dsn)
    print("Database connection successful!")
except Exception as e:
    print("Database connection failed!", str(e))

# Fetch PDF file paths from the database
cursor = conn.cursor()
cursor.execute("SELECT file_path FROM your_pdf_table")  # Replace with your actual query
pdf_paths = cursor.fetchall()

# List to hold the contents of all PDFs
pdf_contents = []

# Read all PDF files from the database
for (file_path,) in pdf_paths:
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        pdf_contents.append(text)

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(pdf_contents)

# Function to search for a query
def search(query):
    query_vector = vectorizer.transform([query])
    results = (X * query_vector.T).toarray()
    return results

# Example of how to use the search function
query_result = search("your search term")

# Close database connection
cursor.close()
conn.close()