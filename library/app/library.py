clients = list(dict())
books = list(tuple())

clients = [
  {
    "first_name": "first_name1",
    "last_name": "last_name1"
  },
  {
    "first_name": "first_name2",
    "last_name": "last_name2"
  },
]

books = [
  {
    "book_title": "book1_title",
    "available": False,
    "author": "book1_author"
  },
  {
    "book_title": "book2_title",
    "available": True,
    "author": "book2_author"
  },
  {
    "book_title": "book3_title",
    "available": True,
    "author": "book3_author"
  },
]

for (index, book) in enumerate(books):
    print(f"Book title: {book.get("book_title")}")
    print(f"""Is book available in the library? {("Yes" if book.get("available") else "No")}""")
    print(f"Book's author: {book.get("author")}")
    print()

def client_exist(client: dict) -> bool:
    """
    Finds the client in the database.
    Returns True if the client exists.
    Returns False if the client doesn't exist.
    """
    return client in clients

# def book_available():
#     return book in get_books("available")

# def lend_book(client, book):
#     if not client_exist:
#         add_client(client)
#     if book_available:
#         clients.get(client) = book

# def return_book(client, book):
#     clients.get(client).remove(book)

# def get_books_list(type_of_books, client=None):
#     if type_of_books == "available":
#         return books.get(type_of_books)

