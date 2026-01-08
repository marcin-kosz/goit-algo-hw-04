from colorama import Fore, init, Style 
import sys
from pathlib import Path

init()

if len(sys.argv) < 2:
    print("Please enter your catalogue path")
    sys.exit(1)

path = sys.argv[1]
parent_folder_path = Path(path)

if not parent_folder_path.exists():
    print(f"Your path '{parent_folder_path}' doesn't exist")
    sys.exit(1)

if not parent_folder_path.is_dir():
    print(f"Your path '{parent_folder_path}' isn't a catalogue")
    sys.exit(1)

def parse_folder(path, level=0):
    indent = "    " * level
    for element in path.iterdir():
        if element.is_dir():
            print(indent + Fore.RED + f"Parse folder: This is folder - {element.name}" + Style.RESET_ALL)
            parse_folder(element, level + 1)
        elif element.is_file():
            print(indent + Fore.GREEN + f"Parse folder: This is file - {element.name}" + Style.RESET_ALL)

print(Fore.RED + f"Parse folder: This is folder - {parent_folder_path.name}" + Style.RESET_ALL)
parse_folder(parent_folder_path)