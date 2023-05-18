""" Random name generator that picks two names from a different tupples, runs as long as user presses enter"""
import random
# colorama package, adds color to text
import colorama
from names import first, last
from colorama import Fore, Style

# initializes colorama module, autoreset= true makes each line reset
colorama.init(autoreset=True)

print("""   Welcome to the Random Name Generator!
        Let's make you a new name!
        """)

while True:
    firstName = random.choice(first)

    lastName = random.choice(last)
    #  fore.red will make any characters after it red, clear it with \033[39m
    print(f"\t{Fore.LIGHTYELLOW_EX} {firstName} {lastName}\n")

    try_again = input(f"Try again? (Press Enter to continue, n to quit)\n >{Fore.CYAN}")

    if try_again.lower() == "n":
        print(f'\033[39m Nice meeting you,{Fore.YELLOW}{Style.BRIGHT} {firstName} {lastName}')
        break
