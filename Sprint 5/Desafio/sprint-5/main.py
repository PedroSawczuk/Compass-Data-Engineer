import sqlite3
import pandas as pd
import boto3
from botocore.exceptions import ClientError
import os

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")
region = 'us-east-1'

s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=region
)

base_bucket_name = 'sprint-5-desafio'

bucket_name = base_bucket_name

try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} criado com sucesso.")

    file_name = 'microdados_ed_basica_2023.csv'
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"Arquivo {file_name} enviado para o bucket {bucket_name}.")
except ClientError as e:
    if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
        print(f"O bucket {bucket_name} já existe e pertence a você.")
    else:
        print("Erro ao criar o bucket ou enviar o arquivo:", e)

file_name_s3 = 'microdados_ed_basica_2023.csv'

file_name_local = 'microdados_ed_basica_2023.csv'

try:
    s3.download_file(bucket_name, file_name_s3, file_name_local)
    print(f"Arquivo {file_name_s3} baixado com sucesso.")
except ClientError as e:
    print("Erro ao baixar o arquivo do S3:", e)

df = pd.read_csv(file_name_local, delimiter=';')

conn = sqlite3.connect(':memory:')

df.to_sql('dados_escolares', conn, index=False)

consulta_1_sql = """
SELECT COUNT(*) AS total_escolas,
       AVG(QT_SALAS_UTILIZADAS) AS media_salas_utilizadas
FROM dados_escolares
WHERE IN_LOCAL_FUNC_PREDIO_ESCOLAR = 1;
"""

resultado_consulta_1 = pd.read_sql_query(consulta_1_sql, conn)

print("\n-------------- consulta 1")
print(resultado_consulta_1)

consulta_2_sql = """
SELECT NO_UF AS UF,
       'Escola Privada' AS 'Tipo de Escola'
FROM dados_escolares
WHERE CO_UF = 11 AND TP_DEPENDENCIA = 2;
"""

resultado_consulta_2 = pd.read_sql_query(consulta_2_sql, conn)

print("\n-------------- consulta 2")
print(resultado_consulta_2)

consulta_3_sql = """
SELECT NO_ENTIDADE AS Entidade,
       CAST(QT_SALAS_UTILIZADAS AS INTEGER) AS 'Salas Utilizadas'
FROM dados_escolares
WHERE CO_UF = 11 AND NO_MUNICIPIO = "Machadinho D'Oeste" AND QT_SALAS_UTILIZADAS IS NOT NULL;
"""

resultado_consulta_3 = pd.read_sql_query(consulta_3_sql, conn)

print("\n-------------- consulta 3")
print(resultado_consulta_3)

consulta_4_sql = """
SELECT NO_ENTIDADE AS Entidade,
       DT_ANO_LETIVO_INICIO AS 'Data de Início do Ano Letivo'
FROM dados_escolares
WHERE CO_UF = 11 AND NO_MUNICIPIO = "Machadinho D'Oeste" AND DT_ANO_LETIVO_INICIO > '01JAN23:00:00:00';
"""

resultado_consulta_4 = pd.read_sql_query(consulta_4_sql, conn)

print("\n-------------- consulta 4")
print(resultado_consulta_4)

consulta_5_sql = """
SELECT NO_ENTIDADE AS Entidade,
       UPPER(NO_MUNICIPIO) AS 'Município (em Maiúsculas)'
FROM dados_escolares
WHERE CO_UF = 11 AND NO_MUNICIPIO = "Machadinho D'Oeste";
"""

resultado_consulta_5 = pd.read_sql_query(consulta_5_sql, conn)

print("\n-------------- consulta 5")
print(resultado_consulta_5)

conn.close()
