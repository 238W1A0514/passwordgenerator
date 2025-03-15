import random
import string
import time
import pyperclip
import pyfiglet
from colorama import Fore, Style


def generate_password():
    print(Fore.CYAN + pyfiglet.figlet_format("PyPassword Generator"))

    while True:
        try:
            nr_letters = int(input(Fore.YELLOW + "🔡 How many letters in your password? "))
            nr_symbols = int(input("🔣 How many symbols? "))
            nr_numbers = int(input("🔢 How many numbers? "))

            if nr_letters + nr_symbols + nr_numbers == 0:
                print(Fore.RED + "⚠ Password must contain at least one character. Try again.")
            else:
                break
        except ValueError:
            print(Fore.RED + "⚠ Invalid input! Please enter a number.")

    print(Fore.GREEN + "\n🔄 Generating your password...", end="")
    time.sleep(1) 

    password_list = (
            random.choices(string.ascii_letters, k=nr_letters) +
            random.choices(string.punctuation, k=nr_symbols) +
            random.choices(string.digits, k=nr_numbers)
    )

    random.shuffle(password_list)
    password = ''.join(password_list)

    print(Fore.CYAN + f"\n✅ Your secure password is: {Fore.MAGENTA}{password}")
    pyperclip.copy(password)
    print(Fore.GREEN + "📋 Password copied to clipboard!")

    print(Style.RESET_ALL) 


generate_password()
