def normalize_currency_code(code: str) -> str:
    code = code.strip().upper()
    if len(code) != 3 or not code.isalpha():
        raise ValueError(f"Некорректный код валюты: '{code}'. Должно быть 3 буквы.")
    return code

def format_amount(amount: float, decimals: int = 2) -> str:
    return f"{amount:,.{decimals}f}"
  
