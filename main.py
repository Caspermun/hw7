# d = {}
# d = {'dict': 1, 'dictionary': 2}
# d = dict.fromkeys(['a', 'b'])
# d = dict(short='dict', long='dictionary')
# d = dict(short='dict')
d = {'key': 'value'}
d.update({'another_key': 'another_value'})  # Дополняет словарь, можно заменять

if __name__ == '__main__':
    # print(d.clear())  # Очищает словарь
    # print(d.copy())  # Копирует словарь
    # print(d.fromkeys(['c', 'd'], 1))  # Создает словарь
    # print(d.get('key'))  # Возвращает значение ключа
    # print(d.items())  # Возвращает пары
    # print(d.keys())  # Возвращает ключи
    # print(d.pop('another_key'))  # Удаляет ключ и возвращает его значение
    # print(d.popitem())  # Удаляет и возвращает последнюю пару
    # print(d.setdefault('long'))  # Возвращает значение ключа
    # print(d.values())  # Возвращает значения