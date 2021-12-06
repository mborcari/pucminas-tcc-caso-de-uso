import requests
from datetime import date, datetime, timedelta
import json
from time import sleep

URL_BASE = 'https://pucminas-ms-pytrader.herokuapp.com/api'

STOCK_TO_CREATE = {
                    "code": "GNDI3",
                    "name": "Notre Dame Intermedica Participacoes SA",
                    "category": "saude",
                    "data_source": "investing"
                }

def create_stock(url, dict_stock):

    url = f'{url}/stock'
    session = requests.Session()
    session.headers.update({
        "content-Type": "application/json",
        "Accept": "application/json",
        "Cache-Control": "no-cache"
    })

    print(f'Iniciando testes as: {datetime.now()}')
    dict_stock = json.dumps(dict_stock)
    return session.post(url=url, data=dict_stock)


def schedule_get_stock_historical_last_30_days(url, stock):

    start_date = datetime.strftime((datetime.today() - timedelta(days=30)), '%d-%m-%Y')
    end_date = datetime.strftime(datetime.today(), '%d-%m-%Y')

    url = f'{url}/get_external_historical'
    session = requests.Session()
    session.headers.update({
        "content-Type": "application/json",
        "Accept": "application/json",
        "Cache-Control": "no-cache"
    })
    body = {
        'code_stock': stock,
        'start_date': start_date,
        'end_date': end_date
    }
    body = json.dumps(body)
    return session.post(url=url, data=body)


def get_stock_historical(url, stock):

    url = f'{url}/historicalstock/{stock}'
    session = requests.Session()
    session.headers.update({
        "content-Type": "application/json",
        "Accept": "application/json",
        "Cache-Control": "no-cache"
    })

    return session.get(url=url)

def delete_stock(url, stock):

    url = f'{url}/stock/{stock}'
    session = requests.Session()
    session.headers.update({
        "content-Type": "application/json",
        "Accept": "application/json",
        "Cache-Control": "no-cache"
    })

    return session.delete(url=url)


if __name__ == '__main__':
    print(f'Iniciando testes as: {datetime.now()}')
    response = create_stock(URL_BASE, STOCK_TO_CREATE)
    print(f'Resultado da criação de um ativo: {response}')
    stock = STOCK_TO_CREATE['code']
    if response.status_code == 201:
        response = schedule_get_stock_historical_last_30_days(URL_BASE, stock)
        if response.status_code == 201:
            print('Agendamento da solicitação do histórico feito com sucesso.')
        sleep(5)
        print('Buscando o histórico.')
        response = get_stock_historical(URL_BASE, stock)
        if response.status_code == 200:
            print(f'{response.content}')
        else:
            print(f'Falha ao buscar histórico do ativo {stock}')
        response = delete_stock(URL_BASE, stock)
        print(f'Resposta do delete do ativo {stock}: {response.status_code}')
    else:
        print(f'Falha ao criar o ativo {stock}, resposta: {response.content}, status {response.status_code}')
    print(f'Testes finalizado as: {datetime.now()}')