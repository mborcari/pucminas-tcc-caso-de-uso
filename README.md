**Os containers estão hospedados na plataforma Heroku.**
Após a primeira requisição, pode ser necessário esperar os container sairem do modo 'idle'. 
Normalmente depois de 10 segundos.

Para teste dos casos de uso.

1 - Instale as dependências do python para os testes.

```
  pip install -r requirements.txt
```

2 - Em seguida, execute os testes:

  Caso de uso para criação de recuperação de histórico. No final o ativo em questão é deletado para repetição do teste.
```
  python create_stock.py
```

   Caso de uso para multiples agendamento de histórico dos ativos.
```
  python get_multiples_historical_data.py
```

   Caso de uso para criação de carteira com adição de um ativo na carteira criada.
```
  python create_portfolio.py
```
