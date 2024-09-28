import hashlib
from pymongo import MongoClient

try:
    cliente = MongoClient('mongodb://localhost:27017/')
    db = cliente['hash_database']
    colecao = db['hashes']
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    exit()

try:
    senha = input("Digite a senha para armazenar: ")

    if senha:
        hash_senha = hashlib.sha256(senha.encode()).hexdigest()

        colecao.insert_one({"hash_senha": hash_senha})
        print("Hash da senha armazenado com sucesso!")

        senha_validacao = input("Digite a senha para validar: ")
        hash_validacao = hashlib.sha256(senha_validacao.encode()).hexdigest()

        if hash_validacao == hash_senha:
            print("Senha válida.")
        else:
            print("Senha inválida.")
    else:
        print("Ocorreu um erro.")
except Exception as e:
    print(f"Erro: {e}")