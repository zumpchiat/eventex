# Eventex

Sistemas de eventos


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes.

```commandline

git clone git@github:zumpchiat/eventex.git wttd
cd wttd
python3 -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python3 manage.py test

```

## Como fazer deploy?

1. Configure seu serviço de hospedagem para Django.
2. Defina as variáveis de instância.
3. Defina o Debug=False
4. Configure o serviço de email.