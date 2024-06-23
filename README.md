# Automação de backup para MySQL
Este projeto contém um script Python para automatizar o backup de um banco de dados MySQL.
O script lê a configuração do banco de dados a partir de variáveis ​​de ambiente, executa um dump do banco de dados usando mysqldump, compacta o arquivo de dump usando gzip e agenda esse backup para ser executado diariamente em um horário especificado.

## Requisitos 
1. Python 3.x
2. MySQL server
3. Utilitário mysqldump
4. Pacotes listados no arquivo requirements.txt
5. Arquivo .env com as variáveis do banco

## Intruções de uso

````
1. python -m venv venv
2. source venv/bin/activate 
3. pip install -r requirements.txt
4. python3 backup.py
````