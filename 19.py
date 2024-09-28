from cryptography.fernet import Fernet
from pymongo import MongoClient

try:
    cliente = MongoClient('mongodb://localhost:27017/')
    db = cliente['fernet_database']
    colecao = db['mensagens']
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    exit()

chave = Fernet.generate_key()
fernet = Fernet(chave)

while True:
    mensagem = input("Digite uma mensagem para criptografar (ou 'sair' para encerrar): ")
    if mensagem.lower() == 'sair':
        break
    mensagem_criptografada = fernet.encrypt(mensagem.encode())
    colecao.insert_one({"mensagem_criptografada": mensagem_criptografada.decode()})

print("Mensagens criptografadas e armazenadas no MongoDB.")
