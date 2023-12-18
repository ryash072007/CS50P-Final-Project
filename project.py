import json


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
        print("    ")
        for i in range(len(books_borrowed)):
            name, issue_data, return_date = books_borrowed[i]
            print(f"{i}. '{name}' borrowed at time {issue_date} is due at {return_date}")


def list_returned():
    books_returned = user_data["books"]["returned"]
    if len(books_borrowed) == 0:
        print("Currently no returned books")
    else:
        print("Currently returned books: ")
        print("    ")
        for i in range(len(books_borrowed)):
            name, issue_data, returned_date = books_borrowed[i]
            print(f"{i}. '{name}' borrowed at time {issue_date} was returned at {returned_date}")


if __name__ == "__main__":
    main(True)
