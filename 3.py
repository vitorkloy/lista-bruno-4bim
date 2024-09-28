import hashlib
from pymongo import MongoClient

try:
    cliente = MongoClient('mongodb://localhost:27017/')
    colecao = cliente['hash_database']['hashes']
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    exit()

try:
    string = input("Digite a string para gerar o hash: ")
    if string:
        hash_gerado = hashlib.sha256(string.encode()).hexdigest()

        try:
            documento = {"string_original": string, "hash_sha256": hash_gerado}
            colecao.insert_one(documento)
            print("Hash salvo com sucesso no MongoDB.")
        except Exception as e:
            print(f"Erro ao salvar no MongoDB: {e}")
    else:
        print("Ocorreu um erro.")
        exit()
except Exception as e:
    print(f"Erro: {e}")
    exit()