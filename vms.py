# Library Management System - Version 1.1
# Features: issue and return books, fine calculation
def issue_book(book_id, member_id):
  print("Book", book_id, "issued to member", member_id)
def return_book(book_id):
  print("Book", book_id, "returned")
def calculate_fine(days_late, rate=5):
  fine = days_late * rate
  print("Fine = Rs.", fine)
  return fine
