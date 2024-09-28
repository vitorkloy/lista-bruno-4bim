import hashlib

try:
    senha = input("Digite a senha: ")

    if senha:
        senha_bytes = senha.encode()
        hash_sha256 = hashlib.sha256(senha_bytes).hexdigest()

        print(f"Hash SHA-256 da senha: {hash_sha256}")
    else:
        print("Ocorreu um erro.")
        exit()
except Exception as e:
    print(f"Erro: {e}")
    exit()