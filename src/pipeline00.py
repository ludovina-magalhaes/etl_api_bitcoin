# Biblioteca para fazer requisições HTTP
# BBDD NoSQL para armazenar os dados
# Biblioteca para manipular tempo e pausas na execução
# Importa datetime para capturar o timestamp

import requests  
from tinydb import TinyDB  
import time  
from datetime import datetime  

# Função para extrair dados do preço do Bitcoin na API da Coinbase
def extract_bitcoin_data():
    url = "https://api.coinbase.com/v2/prices/spot" 
    response = requests.get(url)  
    data = response.json()  # Converte a resposta para um dicionário Python (JSON)
    return data  

# Função para transformar os dados extraídos
def transform_bitcoin_data(data):
    valor = data['data']['amount']  
    criptomoeda = data['data']['base']  
    moeda = data['data']['currency']  
    timestamp = datetime.now().timestamp()  # Captura o timestamp atual

    # Cria um dicionário estruturado com os dados transformados
    transformed_data = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,  
        "timestamp": timestamp
    }  
    return transformed_data  # Retorna os dados transformados

# Função para carregar os dados transformados para uma BBDD TinyDB
def load_bitcoin_data(data, db_name="bitcoin_json"):
    db = TinyDB(db_name)  # Inicializa a BBDD TinyDB com o nome fornecido
    db.insert(data)  # Insere os dados transformados na BBDD
    print("Carregamento foi concluído com sucesso!")  

# Execução principal do script
if __name__ == "__main__":
    data = extract_bitcoin_data()  # Chama a função de extração
    transformed_data = transform_bitcoin_data(data)  # Transforma os dados extraídos
    load_bitcoin_data(transformed_data)  # Carrega os dados na BBDD
    time.sleep(20)  # Faz uma pausa de 20 segundos antes de encerrar o script

