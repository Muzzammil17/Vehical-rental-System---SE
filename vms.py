# Library Management System - Version 2.0
# Features: issue/return books, fine calculation, online catalogue search
catalogue = ["DBMS", "Operating Systems", "Computer Networks"]
def issue_book(book_id, member_id):
  print("Book", book_id, "issued to member", member_id)
def return_book(book_id):
  print("Book", book_id, "returned")
def calculate_fine(days_late, rate=5):
  fine = days_late * rate
  print("Fine = Rs.", fine)
  return fine
def search_book(title):
  if title in catalogue:
    print(title, "is available")
  else:
    print(title, "not found")
