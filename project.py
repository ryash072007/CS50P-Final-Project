username = None


def main():
    print("-----------------Library Management System Login-----------------")
    username = get_valid_input("Enter library username: ")


def get_valid_input(text: str = "", only_digit: bool = False, drange: tuple = (0, 10)):
    while True:
        data = input(text)
        if only_digit:
            if not (data.isdigit() and len(data) == 1) or not (int(data) in range(drange[0], drange[1])):
                print(f"Enter valid digit in range {drange[0]} to {drange[1]}")
                continue
        return data
            

def get_user_password(_username: str):
    pass


if __name__ == "__main__":
    main()
