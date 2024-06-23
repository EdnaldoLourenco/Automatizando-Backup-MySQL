from decouple import config # Função config  para ler variáveis de ambiente do arquivo .env
from pathlib import Path # Importando Path para manipulação de caminhos de arquivos e diretórios
from datetime import datetime # Importando datetime para manipulação de datas e horas
import subprocess # Importando subprocess para execução de comandos do sistema operacional
import gzip # Importando gzip para compressão de arquivos
import os # Importando os para operações com o sistema operacional
import schedule # Importando schedule para agendamento de tarefas
from time import sleep # Importando sleep para pausar a execução do script por um período de tempo

# Lê as configurações do banco de dados a partir das variáveis de ambiente
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')

def backup_database():
    # Diretório onde os backups serão salvos
    backup_dir = Path(__file__).resolve().parent

    # Cria o nome do arquivo de backup com o nome do banco de dados e a data/hora atual
    file_name = f'{DB_NAME}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}'
    # Define o caminho completo do arquivo de backup
    backup_path = f'{backup_dir}/{file_name}.sql'
    # Comando para fazer o dump do banco de dados usando mysqldump
    mysql_dump_command = f'mysqldump -h {DB_HOST} -P {DB_PORT} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {backup_path}'
    # Executa o comando de dump do banco de dados
    subprocess.run(mysql_dump_command, shell=True, check=True)
    # Caminho completo do arquivo de backup comprimido
    compress_backup_path = f'{backup_dir}/{file_name}.sql.gz'
    # Comprimindo o arquivo
    with open(backup_path, 'rb') as original_file:
        with gzip.open(compress_backup_path, 'wb') as compress_file:
            compress_file.write(original_file.read())

    # Remove o arquivo de backup original, deixando apenas o arquivo comprimido
    os.remove(backup_path)

# Agenda a execução da função de backup todos os dias às 22:00 (Horário da Máquina que está executando)
schedule.every().day.at('22:00').do(backup_database)
# Loop infinito para manter o script em execução e verificar tarefas agendadas
while True:
    print('Analisando')
    schedule.run_pending()
    sleep(60)