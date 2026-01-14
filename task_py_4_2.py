from pathlib import Path

path = Path("/Users/marcinkosz/Desktop/Dokumenty/Projekty_GoIT/repozytoria/goit-algo-hw-04/cats_info.txt")

def get_cats_info(path): 
    try:
        cats = []
        with open(path, 'r', encoding='utf-8') as cats_info:
            for line in cats_info:
                clean_line = line.strip()
                if not clean_line:   
                    continue
                parts = clean_line.split(',')
                cat = {"id": parts[0], "name": parts[1], "age": parts[2]}
                cats.append(cat)
        
        return cats

    except FileNotFoundError: 
        print("File not found, check if the path is correct")
    except (ValueError, IndexError):
        print("Wrong data, check your file")

print(get_cats_info(path))
