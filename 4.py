import hashlib
from pymongo import MongoClient

try:
    cliente = MongoClient('mongodb://localhost:27017/')
    colecao = cliente['hash_database']['hashes']
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    exit()

try:
    string = input("Digite a string para comparar o hash: ")

    if string:
        hash_gerado = hashlib.sha256(string.encode()).hexdigest()
    else:
        print("Ocorreu um erro.")
        exit()
    try:
        documento = colecao.find_one({"string_original": string})
        if documento:
            hash_armazenado = documento['hash_sha256']
        else:
            print("Hash não encontrado no MongoDB.")
            exit()
    except Exception as e:
        print(f"Erro ao buscar no MongoDB: {e}")
        exit()

    if hash_gerado == hash_armazenado:
        print("Os hashes são iguais!")
    else:
        print("Os hashes são diferentes.")
except Exception as e:
    print(f"Erro: {e}")
    exit()


