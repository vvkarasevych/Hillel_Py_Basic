import json

# создаем словарь x:
x = {
    "name": "Viktor",
    "age": 30,
    "city": "Minsk"
}
# конвертируем в JSON:
y = json.dumps(x)
# в результате получаем строк JSON:
print(y)
