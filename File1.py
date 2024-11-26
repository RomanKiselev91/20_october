password = input()


if password[0].istitle() and password[-1].isdigit() and password != '' and len(password) >= 3 and password.isspace() == True:
    print(True)
else:
    print(False)