# Grace - ERP in cloud

Solução de Gestão Empresarial Web (em CloudComputing) direcionado para igrejas.

[![Build Status](https://travis-ci.org/EliteDevelopers/GraceERP.svg?branch=master)](https://travis-ci.org/EliteDevelopers/GraceERP)
[![Code Health](https://landscape.io/github/EliteDevelopers/GraceERP/master/landscape.svg?style=flat)](https://landscape.io/github/EliteDevelopers/GraceERP/master)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:EliteDevelopers/GraceERP.git GraceCloudERP
cd GraceERP
python -m venv .GraceCloudERP
source .GraceCloudERP/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRE_KEY=`manage generate_secret_key`
heroku config:set DEBUG=False
# Configure o email
git push heroku master --force
```