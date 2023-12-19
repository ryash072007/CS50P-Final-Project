from project import get_valid_input, main, sign_in

def test_get_valid_input():
    assert(get_valid_input("", input_data = "Hi") == "Hi")
    assert(get_valid_input("", True, (0,2), input_data = "1") == 1)

def test_main():
    assert(main(False, "0") == "signin")
    assert(main(False, "1") == "register")

def test_sign_in():
    assert(sign_in("ryash", "yash2327raj") == True)
    assert(sign_in("ryash", "yash2327raj*") == False)
    assert(sign_in("random", "yash2327raj*") == False)