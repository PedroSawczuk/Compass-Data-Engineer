from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from datetime import datetime
import uuid

# Inicializar o contexto do Glue
glueContext = GlueContext(SparkContext.getOrCreate())

# Obter o SparkSession do GlueContext
spark = glueContext.spark_session

# Caminho do arquivo JSON no S3
json_arquivo = 's3://data-lake-pedro-sawczuk/Raw/TMDB/JSON/2024/06/16/filmes_1.json'

# Ler dados do arquivo JSON
df = spark.read.json(json_arquivo)

# Remover campos indesejados
remover_campos = ['tituloOriginal', 'generoArtista', 'personagem', 'nomeArtista',
                    'anoNascimento', 'anoFalecimento', 'profissao', 'titulosMaisConhecidos']

df_cleaned = df.drop(*remover_campos)

# Filtrar apenas os filmes do gênero 'Fantasy' e lançados até o ano 2000
df_fantasy = df_cleaned.filter((col('genero') == 'Fantasy') & (col('anoLancamento') <= 2000))

# Remover filmes com tempoMinutos vazios (\\N)
df_fantasy = df_fantasy.filter(df_fantasy['tempoMinutos'] != '\\N')

# Gerar um nome aleatório para o arquivo Parquet
arquivo_nome = f'{uuid.uuid4()}.parquet'

# Caminho completo no S3 para o arquivo Parquet
saida_json = f's3://data-lake-pedro-sawczuk/TRUSTED/JSON/MOVIES/{datetime.now().strftime("%Y/%m/%d/")}{arquivo_nome}'

# Salvar os dados em formato Parquet no S3
df_fantasy.write.mode('overwrite').parquet(saida_json)

