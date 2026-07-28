import requests
from .exceptions import APIError, CurrencyNotFoundError
from .cache import Cache

API_URL = "https://api.frankfurter.app"
cache = Cache()

def get_currencies():
    """Возвращает словарь {'USD': 'United States Dollar', ...}"""
    cached = cache.get("currencies")
    if cached:
        return cached

    response = requests.get(f"{API_URL}/currencies", timeout=5)
    if response.status_code != 200:
        raise APIError("Не удалось получить список валют")
    data = response.json()
    cache.set("currencies", data)
    return data

def get_exchange_rate(from_cur, to_cur):
    """Возвращает сколько to_cur стоит 1 from_cur."""
    key = f"{from_cur}_{to_cur}"
    cached = cache.get(key)
    if cached is not None:
        return cached

    params = {"from": from_cur, "to": to_cur}
    response = requests.get(f"{API_URL}/latest", params=params, timeout=5)
    if response.status_code == 404:
        raise CurrencyNotFoundError(f"Валюта {from_cur} или {to_cur} не найдена")
    if response.status_code != 200:
        raise APIError("Ошибка API")
    data = response.json()
    rate = data["rates"].get(to_cur)
    if rate is None:
        raise CurrencyNotFoundError(f"Курс для {to_cur} не найден")
    cache.set(key, rate)
    return rate

def get_historical_rate(from_cur, to_cur, date):
    """На конкретную дату ('2025-01-01')"""
    key = f"{from_cur}_{to_cur}_{date}"
    cached = cache.get(key)
    if cached is not None:
        return cached

    response = requests.get(f"{API_URL}/{date}", params={"from": from_cur, "to": to_cur}, timeout=5)
    if response.status_code != 200:
        raise APIError("Ошибка получения исторического курса")
    data = response.json()
    rate = data["rates"].get(to_cur)
    if rate is None:
        raise CurrencyNotFoundError(f"Нет курса на {date}")
    cache.set(key, rate)
    return rate
