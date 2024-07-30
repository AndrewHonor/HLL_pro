from functools import wraps
from collections import OrderedDict
import requests
import psutil  # Для вимірювання пам'яті


def cache(max_limit=64):
    """
    Декоратор для кешування результатів функцій
    """

    def internal(f):


        @wraps(f)
        def deco(*args, **kwargs):
            # Словник для зберігання кешованих результатів
            cache_dict = OrderedDict()
            # Словник для відстеження кількості використань ключів
            usage_count = {}
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


        return deco

    return internal


def measure_memory(f):
    """Декоратор для вимірювання використання пам'яті"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        memory_info_do = process.memory_info().rss
        result = f(*args, **kwargs)
        memory_info_pisla = process.memory_info().rss
        print(f"Використання пам'яті: {memory_info_pisla - memory_info_do} байт")

        return result

    return wrapper


@cache(max_limit=64)
@measure_memory
def fetch_url(url, first_n=100):
    """Отримує вміст за вказаним URL"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


# Виклик функції:
url_content = fetch_url("https://www.example.com", first_n=200)
print("Закешований вміст:")
print(url_content)

