from functools import wraps
from collections import OrderedDict
import requests
import psutil  # Для вимірювання пам'яті

def cache(max_limit=64):
    """
    Декоратор для кешування результатів функцій.

    Параметри:
        - max_limit (int): Максимальна кількість елементів у кеші (за замовчуванням 64).

    Приклад використання:
        @cache(max_limit=10)
        def fetch_url(url, first_n=100):
            \"\"\"Отримує вміст за вказаним URL\"\"\"
            res = requests.get(url)
            return res.content[:first_n] if first_n else res.content

    Виклик функції:
        url_content = fetch_url("https://www.example.com", first_n=200)
        print(url_content)

        # Вивід кешу:
        fetch_url.print_cache()

        # Вимірювання пам'яті:
        fetch_url.measure_memory()
    """
    def internal(f):
        # Словник для зберігання кешованих результатів
        cache_dict = OrderedDict()
        # Словник для відстеження кількості використань ключів
        usage_count = {}

        @wraps(f)
        def deco(*args, **kwargs):
            # Створюємо унікальний ключ на основі аргументів
            cache_key = (args, tuple(kwargs.items()))

            if cache_key in cache_dict:
                # Переміщуємо ключ в кінець словника (LFU-підхід)
                cache_dict.move_to_end(cache_key, last=True)
                # Збільшуємо лічильник використань
                usage_count[cache_key] += 1
                return cache_dict[cache_key]
            else:
                result = f(*args, **kwargs)
                cache_dict[cache_key] = result
                usage_count[cache_key] = 1

                if len(cache_dict) > max_limit:
                    # Знаходимо ключ з найменшою кількістю використань
                    min_usage_key = min(usage_count, key=usage_count.get)
                    # Видаляємо цей ключ з кешу
                    del cache_dict[min_usage_key]
                    del usage_count[min_usage_key]

                return result

        def print_cache():
            """Виводить весь кеш"""
            print("Кеш:")
            for key, value in cache_dict.items():
                print(f"{key}: {value}")

        def measure_memory():
            """Вимірює використання пам'яті"""
            process = psutil.Process()
            memory_info = process.memory_info().rss
            print(f"Використання пам'яті: {memory_info} байт")

        deco.print_cache = print_cache
        deco.measure_memory = measure_memory
        return deco

    return internal

@cache(max_limit=64)
def fetch_url(url, first_n=100):
    """Отримує вміст за вказаним URL"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

# Виклик функції:
url_content = fetch_url("https://www.example.com", first_n=200)
print("Закешований вміст:")
print(url_content)

# Вивід кешу:
fetch_url.print_cache()

# Вимірювання пам'яті:
fetch_url.measure_memory()
