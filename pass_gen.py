import random
import time
import os
from colorama import Fore

def password_gen():
    os.system('cls')
    characters = "ABCDEFGHIJKLMNOPRSTUWXYZabcdefghijklmnoprstuwxyz1234567890!@#$&_"
    print(f"""{Fore.LIGHTRED_EX}
███╗   ███╗ ██████╗ ███╗   ██╗███████╗ █████╗ 
████╗ ████║██╔═══██╗████╗  ██║╚══███╔╝██╔══██╗
██╔████╔██║██║   ██║██╔██╗ ██║  ███╔╝ ███████║
██║╚██╔╝██║██║   ██║██║╚██╗██║ ███╔╝  ██╔══██║
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
    {Fore.RESET}""")
    pass_length = input(f"{Fore.LIGHTRED_EX}[+]{Fore.RESET} Password length {Fore.LIGHTGREEN_EX}>>>{Fore.RESET} ")
    generated_password = "".join(random.choice(characters) for x in range(int(pass_length)))
    print(f"\n{Fore.LIGHTRED_EX}[+]{Fore.RESET} Generated password {Fore.LIGHTGREEN_EX}>>>{Fore.RESET} {generated_password}")
    print(f"\n{Fore.LIGHTRED_EX}[+]{Fore.RESET} auto close in 1 minute\n")
    time.sleep(60)

password_gen()