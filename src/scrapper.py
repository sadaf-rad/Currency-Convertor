import requests
from bs4 import BeautifulSoup

def get_eur_to_toman():
    url = "https://www.bon-bast.com/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        eur_toman = soup.find("span", {"id": "eur1_top"})
        if eur_toman:
            return float(eur_toman.text.strip().replace(',', ''))
    return None