from cryptography.fernet import Fernet
from pymongo import MongoClient

try:
    cliente = MongoClient('mongodb://localhost:27017/')
    colecao_mensagens = cliente['hash_database']['mensagens']
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    exit()

try:
    chave = Fernet.generate_key()
    fernet = Fernet(chave)

    mensagem = input("Digite a mensagem para criptografar: ")

    if mensagem:
        mensagem_criptografada = fernet.encrypt(mensagem.encode())
        colecao_mensagens.insert_one({"chave": chave.decode(), "mensagem_criptografada": mensagem_criptografada.decode()})

        print("Mensagem criptografada e armazenada no MongoDB.")

        documento = colecao_mensagens.find_one()
        if documento:
            chave = documento['chave'].encode()
            mensagem_criptografada = documento['mensagem_criptografada'].encode()
            fernet = Fernet(chave)
            mensagem_descriptografada = fernet.decrypt(mensagem_criptografada).decode()
            print("Mensagem descriptografada:", mensagem_descriptografada)
        else:
            print("Nenhuma mensagem criptografada encontrada.")
    else:
        print("Ocorreu um erro.")
        exit()
except Exception as e:
    print(f"Erro: {e}")