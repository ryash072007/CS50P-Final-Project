username = None
user_data = None

def main():
    print("-----------------Library Management System Login-----------------")
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
    username = get_valid_input("Enter library username: ").lower()
    data_file = None
    try:
        data_file = open(f"library_data/{username}.data", "r")
    except:
        print(f"Username '{username}' does not exist! Try again!")
        sign_in()
    user_password = data_file.readline().strip()
    user_data = data_file.readlines()
    data_file.close()
    
    if get_valid_input("Enter password: ") != user_password:
        print("Incorrect password!")
        sign_in()
    else:
        print("Successfully Signed In!")
        dashboard()
  

def dashboard():
    pass


if __name__ == "__main__":
    main()
