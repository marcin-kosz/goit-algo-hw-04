from pathlib import Path

path = Path("/Users/marcinkosz/Desktop/Dokumenty/Projekty_GoIT/repozytoria/goit-algo-hw-04/Salaries.txt")

def total_salary(path): 
    try:
        salaries_list = []
        with open(path, 'r', encoding='utf-8') as salaries:
            for line in salaries:
                clean_line = line.strip()
                if not clean_line:   
                    continue
                parts = clean_line.split(',')
                salary = float(parts[1])
                salaries_list.append(salary)
        
        total_salaries = sum(salaries_list)
        average_salary = sum(salaries_list) / len(salaries_list)
        
        return total_salaries, average_salary

    except FileNotFoundError: 
        print("File not found, check if the path is correct")
    except (ValueError, IndexError):
        print("Wrong data, check your file")


total_salary(path)
