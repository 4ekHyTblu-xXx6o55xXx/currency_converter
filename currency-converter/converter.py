from .api import get_exchange_rate, get_historical_rate

def convert(amount, from_cur, to_cur, date=None):
    if date:
        rate = get_historical_rate(from_cur, to_cur, date)
    else:
        rate = get_exchange_rate(from_cur, to_cur)
    return amount * rate