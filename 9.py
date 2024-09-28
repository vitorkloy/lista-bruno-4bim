from cryptography.fernet import Fernet
from pymongo import MongoClient

try: 
    cliente = MongoClient('mongodb://localhost:27017/')
    colecao = cliente['hash_database']['hashes']
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    exit()

try:
    chave = Fernet.generate_key()
    fernet = Fernet(chave)

    mensagem = input("Digite a mensagem que deseja criptografar: ")

    if mensagem:    
        mensagem_criptografada = fernet.encrypt(mensagem.encode())

        colecao.insert_one({
            "chave": chave.decode(),
            "mensagem_criptografada": mensagem_criptografada.decode()
        })

        print("Mensagem criptografada armazenada com sucesso!")
    else:
        print("Ocorreu um erro.")
        exit()
except Exception as e:
    print(f"Erro: {e}")