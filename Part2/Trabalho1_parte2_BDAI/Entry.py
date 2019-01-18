import User
import datetime


def loggin():
    print("Logging in\n")
    username = input("Username: ")
    password = input("Password: ")

    user = User.search_user(user_name=username)
    try:
        if user[2] == password:
            return user
        else:
            return None
    except Exception as error:
        return None


def signin():
    print("Signing in\n")
    username = input("Choose username: ")
    while True:
        user = User.search_user(user_name=username)
        if user is None:
            break
        else:
            print("Username already exists.")
            username = input("Choose username: ")

    password = input("Choose password: ")
    tipo = input("admin or user? ")
    data_entrada = str(datetime.datetime.now().date())

    try:
        User.add_user(nome=username, password=password, data_entrada=data_entrada, tipo=tipo)
        return 1
    except Exception as error:
        return error

