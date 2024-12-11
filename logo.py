import os

def clear_func():
    if os.name == "nt":
       os.system("cls")
    else:
       os.system("clear")
    
clear_func()


def display_responsive_logo():
    logo = """
/$$      /$$                              /$$  /$$$$$$          
| $$$    /$$$                             |__/ /$$__  $$         
| $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$$$$$$ /$$| $$  \__//$$   /$$
| $$ $$/$$ $$ |____  $$ /$$_____//$$_____/| $$| $$$$   | $$  | $$
| $$  $$$| $$  /$$$$$$$|  $$$$$$|  $$$$$$ | $$| $$_/   | $$  | $$
| $$\\  $ | $$ /$$__  $$ \\____  $$\\____  $$| $$| $$     | $$  | $$
| $$ \\/  | $$|  $$$$$$$ /$$$$$$$//$$$$$$$/| $$| $$     |  $$$$$$$
|__/     |__/ \\_______/|_______/|_______/ |__/|__/      \\____  $$
                                                     /$$  | $$
                                                    |  $$$$$$/
                                                     \\______/  
    """
    terminal_width = os.get_terminal_size().columns
    logo_lines = logo.strip().split("\n")
    for line in logo_lines:
        print(line.center(terminal_width))  # Center-align based on terminal width

display_responsive_logo()
