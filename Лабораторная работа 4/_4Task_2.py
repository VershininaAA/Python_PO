import json
import csv
from pathlib import Path

def convert_csv_to_json(input_path: str, output_path: str) -> None:
    try:
        if not Path(input_path).exists():
            raise FileNotFoundError(f"Файл {input_path} не найден")
        
        with open(input_path, mode='r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
            
            if not data:
                raise ValueError("CSV файл не содержит данных")

        with open(output_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
            
        print(f"Успешно конвертировано в {output_path}")
        
    except json.JSONDecodeError as e:
        print(f"Ошибка JSON: {str(e)}")
    except csv.Error as e:
        print(f"Ошибка CSV: {str(e)}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == '__main__':
    INPUT_CSV = "input.csv"
    OUTPUT_JSON = "output.json"
    
    convert_csv_to_json(INPUT_CSV, OUTPUT_JSON)
    
    try:
        with open(OUTPUT_JSON, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("Результат не был создан из-за ошибки")
