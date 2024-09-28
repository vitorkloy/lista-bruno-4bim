from cryptography.fernet import Fernet

try:
    chave = Fernet.generate_key()
    fernet = Fernet(chave)

    mensagem_original = "Esta é uma mensagem secreta."
    print("\nMensagem original:", mensagem_original)

    dados_criptografados = fernet.encrypt(mensagem_original.encode())
    print("Mensagem criptografada:", dados_criptografados.decode())

    dados_descriptografados = fernet.decrypt(dados_criptografados)
    print("Mensagem descriptografada:", dados_descriptografados.decode())
except Exception as e:
    print(f"Erro: {e}")