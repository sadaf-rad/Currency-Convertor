import requests
from cachetools import cached, TTLCache
from scrapper import get_eur_to_toman

cache = TTLCache(maxsize=100, ttl=3*60*60)

@cached(cache)
def get_exchange_rate(base_currency, target_currency):
    if base_currency == 'IRT' or target_currency == 'IRT':
        eur_to_toman = get_eur_to_toman()
        if target_currency == 'IRT':
            if base_currency == 'EUR':
                return eur_to_toman
            else:
                url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
                response = requests.get(url)
                if response.status_code != 200:
                    return None
                base_to_eur = response.json()['rates'].get('EUR', None)
                return base_to_eur * eur_to_toman
        elif base_currency == 'IRT':
            if target_currency == 'EUR':
                return 1 / eur_to_toman
            else:
                url = f"https://api.exchangerate-api.com/v4/latest/{target_currency}"
                response = requests.get(url)
                if response.status_code != 200:
                    return None
                target_to_eur = response.json()['rates'].get('EUR', None)
                return target_to_eur / eur_to_toman
    if base_currency == target_currency:
        return 1
            
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['rates'].get(target_currency, None)

def convert_currency(amount, exchange_rate):
    if exchange_rate is None:
        return None
    return amount * exchange_rate

if __name__ == '__main__':
    base_currency = input("Enter base currency: ")
    target_currency = input("Enter target currency: ")
    amount = float(input("Enter amount: "))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_currency(amount, exchange_rate)
    print(f"{amount} {base_currency} is {converted_amount} {target_currency}")