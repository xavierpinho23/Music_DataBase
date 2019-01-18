# Main
import Entry
import AdminMenu
import ClientMenu

print(">>>>>>>>>>>>>> Welcome to AllMusic23 <<<<<<<<<<<<<<<<<")

user = None
choice = 3

# -------------------------------------------------------------#
# ----------------- User logs or signs in ---------------------#
# -------------------------------------------------------------#

while choice != 0:
	choice = input("Choose [1] to Log in or [2] to Sign in: ")
	if choice == "1":
		user = Entry.loggin()
		if user is None:
			print("Username and password don't match.")
		else:
			print("Welcome")
			choice = 0

	elif choice == "2":
		user = Entry.signin()
		if user == 1:
			print("You're signed in! Proceed to Log in.")
		else:
			print("Something went wrong")

user_type = user[4]

if user_type.lower() == 'admin':
	AdminMenu.menu(user[0])
elif user_type.lower() == "user":
	ClientMenu.menu(user[0])
