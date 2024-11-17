
import json


def task(file_path: str) -> float:
    total = 0.0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            if 'score' in item and 'weight' in item:
                total += item['score'] * item['weight']
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при обработке файла: {e}")

    return round(total, 3)


file_path = "input.json"

result = task(file_path)
print(result)

