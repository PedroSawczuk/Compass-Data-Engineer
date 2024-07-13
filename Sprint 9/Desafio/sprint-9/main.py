import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql import SQLContext
from pyspark.sql.functions import col, when, monotonically_increasing_id

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
sqlContext = SQLContext(sc)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# --- Carregar arquivo .parquet
data_arquivo = spark.read.parquet("s3://data-lake-pedro-sawczuk/TRUSTED/CSV/MOVIES/2024/06/24/dd57c946-9ddf-4c65-9c05-ccdfe09b0478.parquet")

#--- Criando a tabela "correlação" 
correlacao = data_arquivo.select(
    col("id").alias("id_correlacao"),
    col("tituloPincipal").alias("titulo_filme"),
    col("numeroVotos").alias("numero_votos"),
    col("notaMedia").alias("nota_media")
)
#--- Salvando a tabela "correlação" como parquet 
correlacao.write.mode("overwrite").parquet("s3://data-lake-pedro-sawczuk/REFINED/correlacao/")

#--- Criando a tabela "evolucao_filmes" 
contagem_filmes = data_arquivo.groupBy("anoLancamento").count().withColumnRenamed("count", "quantidade_filmes")
contagem_filmes = contagem_filmes.withColumnRenamed("anoLancamento", "ano_lancamento")
contagem_filmes = contagem_filmes.withColumn("id_evolucao_filmes", col("ano_lancamento"))
contagem_filmes.write.mode("overwrite").parquet("s3://data-lake-pedro-sawczuk/REFINED/evolucao_filmes/") #--- Salvando a tabela "evolucao_filmes" como parquet 

#--- Criando a tabela "evolucao_votos" 
evolucao_votos = data_arquivo.groupBy("anoLancamento").sum("numeroVotos").withColumnRenamed("sum(numeroVotos)", "total_votos")
evolucao_votos = evolucao_votos.withColumnRenamed("anoLancamento", "ano_lancamento")
evolucao_votos = evolucao_votos.withColumn("id_evolucao_votos", col("ano_lancamento"))
evolucao_votos.write.mode("overwrite").parquet("s3://data-lake-pedro-sawczuk/REFINED/evolucao_votos/") #--- Salvando a tabela "evolucao_filmes" como parquet 

#--- Criando a tabela "ranking" 
ranking = data_arquivo.select(
    col("id").alias("id_ranking"),
    col("tituloPincipal").alias("titulo_filme"),
    col("numeroVotos").alias("numero_votos")
)
ranking.write.mode("overwrite").parquet("s3://data-lake-pedro-sawczuk/REFINED/ranking/") #--- Salvando a tabela "ranking" como parquet 

#--- Criando a tabela "distribuicao_duracao" 
bins = [0, 60, 90, 120, 150, 180, float('inf')]
labels = ['0-60', '61-90', '91-120', '121-150', '151-180', '180+'] #--- Contagem minutagem de filmes
data_arquivo = data_arquivo.withColumn("tempoMinutos", col("tempoMinutos").cast("int"))
data_arquivo = data_arquivo.withColumn("faixa_duracao", when(col("tempoMinutos") <= 60, '0-60')
                                     .when((col("tempoMinutos") > 60) & (col("tempoMinutos") <= 90), '61-90')
                                     .when((col("tempoMinutos") > 90) & (col("tempoMinutos") <= 120), '91-120')
                                     .when((col("tempoMinutos") > 120) & (col("tempoMinutos") <= 150), '121-150')
                                     .when((col("tempoMinutos") > 150) & (col("tempoMinutos") <= 180), '151-180')
                                     .otherwise('180+'))

contagem_duracao = data_arquivo.groupBy("faixa_duracao").count().withColumnRenamed("count", "quantidade_filmes")
contagem_duracao = contagem_duracao.withColumn("id_duracao", monotonically_increasing_id())
contagem_duracao.write.mode("overwrite").parquet("s3://data-lake-pedro-sawczuk/REFINED/distribuicao_duracao/") #--- Salvando a tabela "distribuicao_duracao" como parquet 

job.commit()
