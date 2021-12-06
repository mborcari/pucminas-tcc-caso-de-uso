#test  comunication between stock microservicess and stock ETL microservices
import requests
import json
from datetime import datetime

stock_list = ['PETR4', 'ABEV3', 'AGRO3', 'ALPA4', 'ANIM3', 'B3SA3', 'BBAS3', 'BBDC3', 'BRKM5', 'CMIG4']

URL_BASE = 'https://pucminas-ms-pytrader.herokuapp.com/api/get_external_historical'

def run_schedule_get_historical(url, stocks):
    session = requests.Session()
    session.headers.update({
        "content-Type": "application/json",
        "Accept": "application/json",
        "Cache-Control": "no-cache"
    })
    print(f'Iniciando testes as: {datetime.now()}')
    for stock in stocks:
        body = {
                "code_stock": stock,
                'start_date': '01-09-2021',
                'end_date': '01-12-2021'
                }
        body = json.dumps(body)
        r = session.post(url=url, data=body)
        print(f'return {r}')
    print(f'Testes finalizado as: {datetime.now()}')


if __name__ == '__main__':
    run_schedule_get_historical(URL_BASE, stock_list)