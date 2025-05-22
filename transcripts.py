import requests
from utils import get_cjremmett_key
BASE_URL = 'https://cjremmett.com/flask/finance/get-earnings-call-transcript'


def get_earnings_call_transcript(ticker: str, year: int, quarter: int) -> str:
    url = BASE_URL + f'?ticker={ticker}&year={year}&quarter={quarter}'
    headers = {
        'token': get_cjremmett_key('finance_key')
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")
    
    return (response.json())['transcript']