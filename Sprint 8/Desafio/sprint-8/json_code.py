from datetime import datetime
import uuid
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Inicialização do SparkSession (necessário para executar em AWS Glue)
sc = SparkContext()
spark = SparkSession(sc)

# Definindo o caminho do arquivo de entrada no S3
inputFile = "s3://data-lake-pedro-sawczuk/Raw/CSV/MOVIES/movies.csv"

# Lendo o arquivo CSV para um DataFrame do Spark
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", StringType(), True),
    StructField("tempoMinutos", StringType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", StringType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

df = spark.read.csv(inputFile, schema=schema, sep='|', header=False)

# Removendo linhas duplicadas com base nas colunas selecionadas
df = df.dropDuplicates(subset=['id', 'tituloPincipal', 'anoLancamento', 'tempoMinutos', 'genero', 'notaMedia', 'numeroVotos'])

# Filtrando os filmes do gênero 'Fantasy' e com tempoMinutos não vazio
dfFiltered = df.filter((col('genero') == 'Fantasy') & (col('tempoMinutos') != '\\N'))

# Convertendo 'anoLancamento' para numérico e filtrando os filmes até o ano 2000
dfFiltered = dfFiltered.withColumn('anoLancamento', dfFiltered['anoLancamento'].cast(IntegerType()))
dfFinal = dfFiltered.filter(dfFiltered['anoLancamento'] <= 2000)

# Selecionando colunas desejadas
dfFinal = dfFinal.select('id', 'tituloPincipal', 'anoLancamento', 'tempoMinutos', 'genero', 'notaMedia', 'numeroVotos')

# Gerando um nome aleatório único para o arquivo Parquet
randomName = uuid.uuid4()
outputFilename = f'{randomName}.parquet'

# Salvando o DataFrame filtrado em formato Parquet no S3
outputPath = f's3://data-lake-pedro-sawczuk/TRUSTED/CSV/MOVIES/{datetime.now().year}/{datetime.now().month:02d}/{datetime.now().day:02d}/{outputFilename}'
dfFinal.write.parquet(outputPath, mode='overwrite')

