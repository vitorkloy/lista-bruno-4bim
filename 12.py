from cryptography.fernet import Fernet

try:
    with open("chave_fernet.key", "rb") as arquivo:
        chave = arquivo.read()

    fernet = Fernet(chave)
    mensagem = input("Digite a mensagem para criptografar: ")
    
    if mensagem:
        mensagem_criptografada = fernet.encrypt(mensagem.encode())
        print("Mensagem criptografada:", mensagem_criptografada.decode())
except Exception as e:
    print(f"Erro: {e}")