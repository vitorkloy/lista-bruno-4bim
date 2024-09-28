from cryptography.fernet import Fernet
from pymongo import MongoClient

try:
    cliente = MongoClient('mongodb://localhost:27017/')
    colecao_chaves = cliente['hash_database']['chaves']
    colecao_mensagens = cliente['hash_database']['mensagens']
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    exit()

try:
    documento_chave = colecao_chaves.find_one()
    if documento_chave:
        chave = documento_chave['chave'].encode()
        fernet = Fernet(chave)
        documento_mensagem = colecao_mensagens.find_one()
        if documento_mensagem:
            mensagem_criptografada = documento_mensagem['mensagem_criptografada'].encode()
            mensagem_descriptografada = fernet.decrypt(mensagem_criptografada).decode()
            print("Mensagem descriptografada:", mensagem_descriptografada)
        else:
            print("Nenhuma mensagem criptografada encontrada.")
    else:
        print("Nenhuma chave encontrada no MongoDB.")
        exit()
except Exception as e:
    print(f"Erro: {e}")