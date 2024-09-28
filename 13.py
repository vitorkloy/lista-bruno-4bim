from cryptography.fernet import Fernet
from pymongo import MongoClient

try:
    cliente = MongoClient('mongodb://localhost:27017/')
    colecao_chaves = cliente['hash_database']['chaves']
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    exit()

try:
    chave = Fernet.generate_key()

    documento = {"chave": chave.decode()}
        
    if documento:
        colecao_chaves.insert_one(documento)
        print("Chave Fernet gerada e armazenada no MongoDB.")
    else: 
        print("Ocorreu um erro.")
except Exception as e:
    print(f"Erro: {e}")
    exit()