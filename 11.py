from cryptography.fernet import Fernet

try:
    chave = Fernet.generate_key()
    if chave:
        with open("chave_fernet.key", "wb") as arquivo:
            arquivo.write(chave)

        print("Chave Fernet gerada e salva no arquivo.")
    else:
        print("Ocorreu um erro.")
        exit()
except Exception as e:
    print(f"Erro: {e}")