# Comandos Utilizados

- Instalar os pacotes:

`pip install -r requiriments.txt`

- Criar um projeto do Django:

`django-admin startproject proj .`

- Executar o servidor:

`python manage.py runserver`

- Configurar o runserver para rodar/debug direto pelo Pycharm:

- Criar um novo app:

`django-admin startapp cadastros`

- Criar as migrações para serem executadas no BD:

`python manage.py makemigrations`

- Executar as alterações no BD:

`python manage.py migrate`

- Criar um superusuário:

`python manage.py createsuperuser`

- Configurar o pycharm para rodar o python console com suporte ao django:

```
import sys,os, django
print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
django.setup()
```

- Instalar o ipython (para um console mais poderoso):

`pip install ipython`

### Comandos Docker:
- Para rodar direto o docker:

`docker-compose`

- Caso o arquivo docker tenha outro nome:

`docker-compose -f docker-compose.dev.yml(na frente do -f é o nome do arquivo)`

- Para rodar

`docker-compose up`

- Se jogar um -d após o up, ele fica rodando em segundo plano e pode utilizar o terminal
- Para parar é só jogar um down no final

- Para baixar as imagens

`docker-compose build`

TO-DO
===================

- Criar o CRUD de front-end para País e Estados