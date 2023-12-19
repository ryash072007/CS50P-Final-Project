import json
import re
import random
from datetime import date, timedelta


username = None
user_data = None

def main(greet = False):
    if greet: print("-----------------Library Management System Login-----------------")
    match get_valid_input("Do you want to sign in or register: (0 -> Sign In | 1 -> Register) ", True):
        case 0:
            sign_in()
        case 1:
            register()


def get_valid_input(text: str = "", only_digit: bool = False, drange: tuple = (0, 2)):
    while True:
        data = input(text)
        if not data:
            print("Enter non empty text")
            continue
        if only_digit:
            if not (data.isdigit() and len(data) == 1) or not (int(data) in range(drange[0], drange[1])):
                print(f"Enter valid digit in range {drange[0]} to {drange[1]}")
                continue
        return data if not only_digit else int(data)
            

def sign_in():
    global username, user_data
    username = get_valid_input("Enter library username: ").lower()
    data_file = None
    try:
        data_file = open(f"library_data/{username}.data", "r")
    except:
        print(f"Username '{username}' does not exist! Try again!")
        main()
    user_data = json.load(data_file)
    data_file.close()
    
    if get_valid_input("Enter password: ") != user_data["password"]:
        print("Incorrect password!")
        sign_in()
    else:
        print("Successfully Signed In!")
        dashboard()
  

def register():
    username = get_valid_input("Enter new library username: ").lower()
    data_file = None
    try:
        data_file = open(f"library_data/{username}.data", "r")
    except:
        pass
    if data_file:
        data_file.close()
        print(f"Username '{username}' already exists!")
        main()
    else:
        user_data = {
            "password": get_valid_input("Enter new password: "),
            "books": {
                "borrowed": [], # (name, issue_date, supposed_return_date) 
                "returned": [] # (name, issue_date, returned_date) 
            }
        }
        data_file = open(f"library_data/{username}.data", "w")
        json.dump(user_data, data_file)
        data_file.close()
        print("You have successfully registered yourself!")
        dashboard()


def dashboard():
    print("\n--------------------------Dashboard------------------------------")
    # print(user_data)
    match get_valid_input("list borrowed (0) / list returned (1) / borrow more (2) / return more (3): ",
                          True,
                          (0,4)):
        case 0:
            list_borrowed()
        case 1:
            list_returned()
        case 2:
            borrow_more()
        case 3:
            return_more()    


def list_borrowed():
    books_borrowed = user_data["books"]["borrowed"]
    if len(books_borrowed) == 0:
        print("Currently no borrowed books")
    else:
        print("Currently borrowed books: ")
        for i in range(len(books_borrowed)):
            print("    ")
            name, issue_date, return_date = books_borrowed[i]
            print(f"{i}. '{name}' borrowed on {issue_date} is due on {return_date}.")
    dashboard()


def list_returned():
    books_returned = user_data["books"]["returned"]
    if len(books_borrowed) == 0:
        print("Currently no returned books")
    else:
        print("Currently returned books: ")
        print("    ")
        for i in range(len(books_borrowed)):
            name, issue_data, returned_date = books_borrowed[i]
            print(f"{i}. '{name}' borrowed on {issue_date} was returned on {returned_date}")


def borrow_more():
    book_list = None
    match get_valid_input("Search book (0) / List books (1) / Random book (2): ", True, (0,3)):
        case 0:
            search_book()
        case 1:
            list_books()
        case 2:
            choose_random_book()
    borrow_more()


def search_book():
    book_list = None
    with open("book_list.data", "r") as f:
        book_list = f.readlines()
    book_name = get_valid_input("Enter book name: ")
    matching_books = []
    for book in book_list:
        book = book.strip()
        match = re.search(book_name.lower(), book.lower())
        if match:
            matching_books.append(book)
    if not matching_books:
        print("No books match the given search text!")
    else:
        for i in range(len(matching_books)):
            print(f"{i}. {matching_books[i]}")
        borrow_index = get_valid_input("Enter index to borrow that book: ", True, (0, len(matching_books)))
        weeks_to_borrow = get_valid_input("Enter for how many weeks you want to borrow book (1-3): ", True, (1, 4))
        user_data["books"]["borrowed"].append((matching_books[borrow_index], str(date.today()), str(date.today() + timedelta(weeks = weeks_to_borrow))))
        data_file = open(f"library_data/{username}.data", "w")
        json.dump(user_data, data_file)
        data_file.close()
        print("Successfully borrowed book!")


def list_books():
    book_list = []
    with open("book_list.data", "r") as f:
        book_list = f.readlines()
    for i in range(len(book_list)):
        print(f"{i}. {book_list[i].strip()}")


def choose_random_book():
    book_list = []
    with open("book_list.data", "r") as f:
        book_list = f.readlines()
    random_book = random.choice(book_list)
    print(f"'{random_book.strip()}' was randomly chosen for you.")
    match get_valid_input("Accept book (0) / Reroll (1): ", True, (0,2)):
        case 0:
            weeks_to_borrow = get_valid_input("Enter for how many weeks you want to borrow book (1-3): ", True, (1, 4))
            user_data["books"]["borrowed"].append((matching_books[borrow_index], str(date.today()), str(date.today() + timedelta(weeks = weeks_to_borrow))))
            data_file = open(f"library_data/{username}.data", "w")
            json.dump(user_data, data_file)
            data_file.close()
            print("Successfully borrowed book!")
        case 1:
            choose_random_book()

if __name__ == "__main__":
    main(True)
