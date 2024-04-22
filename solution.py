# import requests
# import pandas as pd

# # Read ISBN numbers from the file
# with open('books-isbns.txt', 'r') as file:
#     isbns = file.read().splitlines()

# book_details = []

# # Iterate through each ISBN number
# for isbn in isbns:
#     url = f"https://openlibrary.org/isbn/{isbn}.json"
    
#     try:
#         response = requests.get(url, timeout=2)
#         if response.status_code == 200:
#             book_data = response.json()  # Assuming the response is in JSON format
#             book_details.append(book_data)
#     except requests.exceptions.Timeout:
#         print(f"Timeout occurred for ISBN: {isbn}")

# # Convert the book_details list to a pandas DataFrame for analysis
# df = pd.DataFrame(book_details)
# print(df)

import requests
import pandas as pd

# Read ISBN numbers from the file
with open('books-isbns.txt', 'r') as file:
    isbns = [line.strip() for line in file]

book_details = []

# Function to fetch book details from Open Library API with timeout
def fetch_book_details(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    try:
        response = requests.get(url, timeout=2)  # Timeout set to 2 seconds
        if response.status_code == 200:
            book_data = response.json()
            return book_data
    except requests.exceptions.Timeout:
        print(f"Timeout occurred for ISBN: {isbn}")
    return None

# Fetch book details for each ISBN
for isbn in isbns:
    book_data = fetch_book_details(isbn)
    if book_data:
        book_details.append(book_data)

# Create a DataFrame from the book details
df = pd.DataFrame(book_details)

# Drop duplicates based on the title column
df.drop_duplicates(subset='title', inplace=True)

# Save the results to a .csv file
df.to_csv('book_details.csv', index=False)