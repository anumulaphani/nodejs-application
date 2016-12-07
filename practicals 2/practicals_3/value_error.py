def get_num(lower, upper):
    while (True):
        try:
            user_input = int(input("Enter a number  ({}-{}):".format(lower, upper)))
            if user_input < lower:
                print("Number too low.")
            elif user_input > upper:
                print("please enter a valid number")
            else:
                return user_input
        except ValueError:
            print("Please enter a valid number")