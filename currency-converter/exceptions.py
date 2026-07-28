class CurrencyError(Exception):
    """Главная ошибка проекта"""

class APIError(CurrencyError):
    """Ошибка при обращении к сайту"""

class CurrencyNotFoundError(CurrencyError):
    """Отсутствие данной валюты"""
