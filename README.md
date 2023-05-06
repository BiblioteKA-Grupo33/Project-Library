# BiblioteKA - Project Backend

## Passos ncessários para funcionamento

### Windows

- Iniciar um ambiente virtual com o seguinte comando:
```shell
python -m venv venv
```

- Instalando dependencias do projeto:
```shell
pip install -r requirements.txt
```
- Criar e preencher os dados do arquivo .env seguindo o .env.example:
```shell
SECRET_KEY=

POSTGRES_USERNAME=
POSTGRES_PASSWORD=
POSTGRES_DB_NAME=
POSTGRES_DB_HOST=
POSTGRES_DB_PORT=

EMAIL_HOST= 
EMAIL_PORT= 
EMAIL_HOST_USER= 
EMAIL_HOST_PASSWORD= 
```


Esta aplicação contém relacionamentos com banco de dados. O objetivo dela é permitir a interação do cliente, possibilitando a solicitação de empréstimos de livros e a visualização dos livros listados no banco de dados.

## Infos da Api

Caso queira ter uma visão ampla das rotas e fazer testes da mesma acesse o link abaixo:<br>
<a href= https://biblioteka-grupo33.onrender.com/api/schema/swagger/ _blank=true>Documentação Api</a><br>
É importante deixar claro que algumas rotas requer permissão de admin ou seja usuários normais não consiguiram fazer algumas requisições
