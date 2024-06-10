import boto3
from datetime import datetime
from dotenv import load_dotenv

def uploadS3(nomeArquivo, bucket, objectName):
    s3Client = boto3.client('s3')
    try:
        response = s3Client.upload_file(nomeArquivo, bucket, objectName)
    except Exception as e:
        print(f"Erro: {nomeArquivo}: {e}")
        return False
    return True

def main():
    load_dotenv()  
    nomeBucket = 'desafio-sprint6'

    arquivosCsv = {
        "movies.csv": "/data/movies.csv",
        "series.csv": "/data/series.csv"
    }

    data = datetime.now().strftime("%Y/%m/%d")

    for nomeArquivo, caminhoArquivo in arquivosCsv.items():
        s3ObjectName = f"Raw/Local/CSV/{nomeArquivo.split('.')[0].capitalize()}/{data}/{nomeArquivo}"
        if uploadS3(caminhoArquivo, nomeBucket, s3ObjectName):
            print(f"Enviado: {nomeArquivo} to {s3ObjectName}")
        else:
            print(f"Erro ao enviar {nomeArquivo}")

if __name__ == "__main__":
    main()
