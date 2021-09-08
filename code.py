import hashlib
from colorama import Fore, Back, Style
import os

def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False

def register(password_to_register):
	with open("passwords.txt", "a+") as f:
		f.write(password_to_register.hexdigest() + "\n")

def login_check(password_to_check):
	x = check_if_string_in_file("passwords.txt", password_to_check.hexdigest())
	if x == True:
		print("Correct!")

	elif x == False:
		print("Incorrect.")

def clear_passwords():
	file = open("passwords.txt", "r+")
	file.truncate(0)
	file.close()


print("Welcome! Please choose a option:")
print(Fore.GREEN + """
1) Login
2) Register
3) Clear all passwords
4) Exit
""")


choosen_option = int(input(": "))


if choosen_option == 1:
	os.system("clear")
	print(Fore.BLUE + 'Login Page')
	print()
	entered = input("Enter password: ")
	password_to_be_checked = hashlib.md5(entered.encode())
	login_check(password_to_be_checked)
	exit()



elif choosen_option == 2:
	os.system("clear")
	print(Fore.BLUE + 'Register Page')
	print()
	passworddd = input("Enter password: ")
	hash_object = hashlib.md5(passworddd.encode())
	register(hash_object)
	exit()

elif choosen_option == 3:
	clear_passwords()
	exit()

elif choosen_option == 4:
	exit()

else:
	print("Please choose a valid option.")
