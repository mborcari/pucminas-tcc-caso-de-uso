import requests
import json

URL_LOGIN = 'http://ec2-52-23-254-85.compute-1.amazonaws.com:8080/auth'
URL_PORTFOLIO = 'http://ec2-18-116-63-102.us-east-2.compute.amazonaws.com:8080/portfolio'
URL_PORTFOLIO_ADD_STOCK = 'http://ec2-18-116-63-102.us-east-2.compute.amazonaws.com:8080/portfolio/addAsset'
portfolio_name = 'Teste 100'
stock = 'ABEV3'


def login_user(url):
    session = requests.Session()
    session.headers.update({
        "content-Type": "application/json",
        "Accept": "application/json",
        "Cache-Control": "no-cache"
    })

    body = {
          "email": "teste@gmail.com",
          "password": "mimica"
        }
    body = json.dumps(body)
    return session.post(url=url, data=body)


def create_portfolio(url, token, name):
    session = requests.Session()
    session.headers.update({
        "content-Type": "application/json",
        "Accept": "application/json",
        "Cache-Control": "no-cache",
        "Authorization": build_authorization(token)
    })

    body = {
        'name': name
    }
    body = json.dumps(body)
    return session.post(url, data=body)


def portfolio_add_stock(url, token, portfolio, stock):
    session = requests.Session()
    session.headers.update({
        "content-Type": "application/json",
        "Accept": "application/json",
        "Cache-Control": "no-cache",
        "Authorization": build_authorization(token)
    })

    body = {
        'idPortfolio': portfolio,
        'codeAsset':  stock
    }
    body = json.dumps(body)
    return session.post(url, data=body)


def build_authorization(token):
    return f'Bearer {token}'


if __name__ == '__main__':
    response = login_user(URL_LOGIN)

    content = json.loads(response.content)
    if response.status_code == 200:
        token = content['token']
        print(f'Criando portifolio {portfolio_name}')
        portfolio_response = create_portfolio(URL_PORTFOLIO, token, portfolio_name)
        if portfolio_response.status_code == 201:
            portfolio_id = json.loads(portfolio_response.content)['id']
            print(f'Portifolio {portfolio_name} criado com sucesso, id {portfolio_id}')
            add_response = portfolio_add_stock(URL_PORTFOLIO_ADD_STOCK, token, portfolio_id, stock)
            print(add_response, add_response.content)
            if add_response.status_code == 200:
                print(f'Ativo {stock} adicionado na carteira {portfolio_name}')
            else:
                print(f'Falha ao adicionar o ativo {stock} adicionado na carteira {portfolio_name}')