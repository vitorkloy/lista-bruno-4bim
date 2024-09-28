from cryptography.fernet import Fernet

try:
    chave = Fernet.generate_key()
    print(f"Chave gerada: {chave.decode()}")

    fernet = Fernet(chave)

    mensagem = input("Digite a mensagem para criptografar: ")
    
    if mensagem:
        mensagem_criptografada = fernet.encrypt(mensagem.encode())
        print(f"Mensagem criptografada: {mensagem_criptografada}")

        mensagem_descriptografada = fernet.decrypt(mensagem_criptografada)
        print(f"Mensagem original: {mensagem_descriptografada.decode()}")
    else:
        print("Ocorreu um erro.")
        exit()
except Exception as e:
    print(f"Erro: {e}")
    exit()