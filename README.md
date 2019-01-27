# Eventex
[![Build Status](https://travis-ci.org/diegoarioza/eventex.svg?branch=master)](https://travis-ci.org/diegoarioza/eventex)

Sistemas de Eventos

## Como desenvolver
1. Clone o repositorio
2. Crie um venv com python 3.5
3. Ative o venv
4. Intale as dependencias
5. Configure a instancia com o .env
6. execute os testes

```console
git clone https://github.com/diegoarioza/eventex.git wttd
cd wttd
python -m venv .wttd
source .wwtd/bin/activate
pip install -r install requirements-dev.txt
cp contrib/env-sample .
python manage.py test
```

## Como fazer o deploy
1. Crie uam instancia no heroku
2. Envie as configuracoes para o heroku
3. Defina uma SecretKey segura na instancia
4. Defina Debug=False
5. Configure o serviço de email.
6. Envie o codigo para o heroku
```console
heroku create minhainstancia
heroku config:push
heroku config: set SECRET_KEY=$(python contrib/secret_gen.py)
heroku config:set DEBUG=False
# configuro o email

git push heroku master --force
```