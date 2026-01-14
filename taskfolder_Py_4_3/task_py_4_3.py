from colorama import Fore, init, Style
import sys
from pathlib import Path

init()

def parse_folder(path, level=0):
    indent = "    " * level
    for element in path.iterdir():
        if element.is_dir():
            print(indent + Fore.RED + element.name + Style.RESET_ALL)
            parse_folder(element, level + 1)
        elif element.is_file():
            print(indent + Fore.GREEN + element.name + Style.RESET_ALL)

def main():
    if len(sys.argv) < 2:
        print("Please enter your catalogue path")
        return

    parent_folder_path = Path(sys.argv[1])

    if not parent_folder_path.exists():
        print(f"Your path '{parent_folder_path}' doesn't exist")
        return

    if not parent_folder_path.is_dir():
        print(f"Your path '{parent_folder_path}' isn't a catalogue")
        return

    print(Fore.RED + parent_folder_path.name + Style.RESET_ALL)
    parse_folder(parent_folder_path)

if __name__ == "__main__":
    main()