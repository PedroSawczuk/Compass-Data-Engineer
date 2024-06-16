import pandas as pd
import json
import os
import requests
from datetime import datetime
import boto3

dataDir = "data"
saidaDir = "outputs/movies"

chaveApiTMDB = os.getenv('TMDB_API_KEY')

def buscarFilmeTMDB(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {
        'api_key': chaveApiTMDB,
        'language': 'pt-BR'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

df = pd.read_csv(os.path.join(dataDir, "movies.csv"), sep="|")  
df.drop_duplicates(subset="id", inplace=True)

filtered_df = df[df['genero'].isin(["Sci-Fi", "Fantasy"])]

os.makedirs(saidaDir, exist_ok=True)

grupo = []
grupoSize = 0
grupoIndice = 1

def salvarUploadS3(grupo, idx):
    now = datetime.now()
    ano = now.strftime("%Y")
    mes = now.strftime("%m")
    dia = now.strftime("%d")
    
    s3_path = f"Raw/TMDB/JSON/{ano}/{mes}/{dia}/"
    
    s3_client = boto3.client('s3')
    
    file_name = f"filmes_{idx}.json"
    file_path = os.path.join(saidaDir, file_name)
    
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(grupo, json_file, ensure_ascii=False, indent=4)
    
    s3_key = s3_path + file_name
    s3_client.upload_file(file_path, 'data-lake-pedro-sawczuk', s3_key)
    
for idx, (index, row) in enumerate(filtered_df.iterrows(), start=1):
    movie_data = row.to_dict()
    
    if pd.isna(movie_data.get('profissao')):
        movie_data['profissao'] = ""
    
    tmdb_details = buscarFilmeTMDB(movie_data['id'])
    
    if tmdb_details:
        movie_data['titulo_original'] = tmdb_details.get('original_title', '')
        movie_data['sinopse'] = tmdb_details.get('overview', '')
        movie_data['linguagem_original'] = tmdb_details.get('original_language', '')
        movie_data['popularidade'] = tmdb_details.get('popularity', '')
    
    grupo.append(movie_data)
    
    movie_json = json.dumps(movie_data, ensure_ascii=False, indent=4)
    filmeSize = len(movie_json.encode('utf-8'))
    
    if grupoSize + filmeSize > 10 * 1024 * 1024:
        salvarUploadS3(grupo, grupoIndice)
        grupoIndice += 1
        grupo = []
        grupoSize = 0
    else:
        grupoSize += filmeSize

if grupo:
    salvarUploadS3(grupo, grupoIndice)
